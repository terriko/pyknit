#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more
"""

import argparse
import math
from typing import Set
from pyknit import GaugeSwatch, Chart

VERSION = "pyKnit 0.0.3"


# Increase and decrease functions


def increase_evenly(
    starting_count: int, increase_number: int, in_the_round: bool = False
) -> str:
    """ A function to figure out even spacing for increases """

    if not in_the_round:
        # It's increase+1 so that you don't have increases at either
        # the start or end of a row
        increase_spacing = increase_number + 1
    else:
        increase_spacing = increase_number

    interval = math.floor(starting_count / (increase_spacing))
    remainder = starting_count % increase_spacing

    # first set of increases
    if increase_spacing - remainder > 1:
        instruction_string = f"[k{interval}, m1] * {increase_spacing-remainder} times"
    else:
        instruction_string = f"k{interval}, m1"

    # second set of increases (if needed)
    if remainder > 0:
        if not in_the_round:
            if remainder - 1 > 1:
                instruction_string += (
                    f", [k{interval+1}, m1] * {remainder-1} times, k{interval+1}"
                )
            else:
                instruction_string += f", k{interval+1}, m1, k{interval+1}"
        else:
            if remainder > 1:
                instruction_string += f", [k{interval+1}, m1] * {remainder} times"
            else:
                instruction_string += f", k{interval+1}, m1"

    # if we still need a selvage, add that
    else:
        if not in_the_round:
            instruction_string += f", k{interval}"

    return instruction_string


def decrease_evenly(
    starting_count: int, decrease_number: int, in_the_round: bool = False
):
    """ A function to figure out spacing for decreases """


def sleeve_decreases(
    number_of_rows: int,
    starting_count: int,
    ending_count: int,
    decrease_per_row: int = 2,
) -> str:
    """ A function to figure out a nice even sleeve decrease. """

    # TODO: This function is going to be pretty similar to the decrease_evenly()
    # function.  We may want to combine them later.

    if starting_count <= ending_count:
        print(
            f"Error: No decreases needed, {starting_count} is already smaller than {ending_count}"
        )

    # How many times are we doing the decrease row?
    number_of_decrease_rows = math.floor(
        (starting_count - ending_count) / decrease_per_row
    )
    if ((starting_count - ending_count) % decrease_per_row) > 0:
        # TODO: we could probably do this math for people if we wanted
        print(
            f"Warning: desired decrease doesn't work exactly with a {decrease_per_row} decrease"
        )
        print(
            "Printing the closest alternative but you'll need to add decreases at the end"
        )

    # divide up the number of rows.
    # This gives you a decrease on the first row but padding after the last
    # TODO: make an option for padding both sides, padding neither?

    interval = math.floor(
        (number_of_rows - number_of_decrease_rows) / number_of_decrease_rows
    )
    remainder = (number_of_rows - number_of_decrease_rows) % number_of_decrease_rows

    # If we had any remainder, pad out the early decreases
    instruction_string = ""
    if remainder > 0:
        instruction_string += (
            f"[decrease row, do {interval+1} rows in pattern] * {remainder} times, "
        )
    instruction_string += f"[decrease row, do {interval} rows in pattern] * {number_of_decrease_rows - remainder} times"

    return instruction_string


def main():
    print(VERSION)
    desc = """
    This package is intended for use as a library inside jupyter notebook,
    so that you can see charts as they're parsed.

    For fun, this command line version will take a string and attempt to parse
    it into a python array of individual stitches.
    """
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument(
        "instruction_row",
        help="A row of knitting instructions. e.g. 'k2 p4'",
    )
    args = parser.parse_args()
    legend = {
        "k": "k",
        "p": "p",
        "kfb": "kfb",
        "ssk": "ssk",
        "k2tog": "k2tog",
        "p2tog": "p2tog",
    }

    print(parse_written(args.instruction_row, legend))


if __name__ == "__main__":
    main()
