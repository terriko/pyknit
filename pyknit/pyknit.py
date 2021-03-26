# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

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


def raglan_increases(
    neck_stitches: int,
    arm_stitches: int,
    bust_stitches: int,
    neck_to_bust_rows: int,
    increase_per_increase_row: int = 8,
    armpit_stitches: int = 4,
) -> str:
    """Tool for adjusting raglan sweaters to increase arm size or bust size.

    For a standard raglan, you increase along 4 diagonal lines over the front
    and back of the shoulders.  Each line has an increase on either side.

    Tutorial for a well-documented raglan here:
    https://blog.tincanknits.com/2013/10/25/lets-knit-a-sweater/"""

    # Adjusting from collar to start of raglan
    instruction_string = ""
    # the final stitch count is bust_stitches + 2 * arm stitches
    # but that includes the added armpit stitches on both sides+sleeves
    working_stitches = bust_stitches + (2 * arm_stitches) - (4 * armpit_stitches)

    # Work backwards and see if you get the collar number
    calculated_neck = working_stitches - neck_to_bust_rows * increase_per_increase_row

    # if calculated_neck and neck_stitches don't match, make adjustments

    if calculated_neck > neck_stitches:
        # Add an increase row to go from your actual collar size to raglan start
        instruction_string += "Increase row: "
        instruction_string += increase_evenly(
            neck_stitches, calculated_neck - neck_stitches, in_the_round=True
        )

    if calculated_neck < neck_stitches:
        # you don't need to increase every row in the raglan section
        # We'll put the non-increase rows at the end before the armpit section
        no_increase_rows = 555 # FIXME

    # generate some standard raglan instructions
    # we're assuming the beginning of row is the middle of the back here
    body_start = bust_stitches/2 - neck_to_bust_rows*2 - armpit_stitches

    # in case our count is uneven
    front = math.ceil(body_start)
    back = math.floor(body_start)

    arm = arm_stitches - armpit_stitches - neck_to_bust_rows*2

    instruction_string += f"Marker setup: k{math.floor(back/2)}, pm, k{arm} (arm), pm, "
    instruction_string += f"k{front}, pm, k{arm} (arm), pm k{math.ceil(back/2)}"

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
