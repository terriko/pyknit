#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more
"""

import argparse
import math
import re
from PIL import Image, ImageDraw, ImageFont
from typing import Set

VERSION = "pyKnit 0.0.2"


class Swatch:
    """Information from a gauge swatch"""

    def __init__(
        self,
        row_count: int,
        row_measure: float,
        stitch_count: int,
        stitch_measure: float,
        units: str,
    ):
        self.row_count = row_count
        self.row_measure = row_measure
        self.stitch_count = stitch_count
        self.stitch_measure = stitch_measure
        self.units = units
        # TODO: add yardage/weight for calculations?

    def row_gauge() -> float:
        """ return rows per unit (e.g. cm, inch) number """
        return self.row_count / self.row_measure

    def stitch_gauge() -> float:
        """ return stitches per unit (e.g. cm, inch) number """
        return self.stitch_count / self.stitch_measure

    def measurement_to_stiches(measurement: float) -> int:
        """
        Given a measurement, how many stiches would we need?
        Round to closest stitch.
        """
        return math.round(measurement * stitch_gauge())

    def measurement_to_rows(measurement: float) -> int:
        """
        Given a measurement, how many rows would we need?
        Round to closest number of rows."""
        return math.round(measurement * row_gauge())

    def rows_to_measurement(rows: int) -> float:
        """ figure out how long a number of rows will be """
        return rows / row_gauge()

    def stitches_to_measurement(stitches: int) -> float:
        """ figure out how wide a number of stitches will be """
        return stitches / stitch_gauge()


# Gauge and stich count related functions


def stitch_count(stitch_array: Set[str], legend: Set[str]) -> int:
    if legend:
        # FIXME: Do calculations per stitch
        return len(stitch_array)

    # otherwise, assume every stitch has width=1
    return len(stitch_array)


## Chart and pattern parsing functions


def parse_written(row: str, legend: Set[str]) -> Set[str]:
    """Parse a written set of knitting instructions and print an array of
    stitches using a legend.  This is a stand in for eventually printing a
    chart."""

    stitch_array = []
    for section in row.split(" "):

        patterns = [
            r"([a-z]+[0-9]+[a-z]+)([0-9]*)",  # things like k2tog or m1l
            r"([a-z]+)([0-9]*)",  # things like p4
        ]
        matched_stitch = False
        for pat in patterns:
            result = re.match(pat, section)
            if result and not matched_stitch:
                # only match one pattern per stitch so k2tog doesn't
                # get parsed as k2
                matched_stitch = True
                stitch = result.group(1)
                # set the number or if no number, assume you repeat once
                number = int(result.group(2)) if result.group(2) else 1
                for i in range(0, number):
                    if stitch in legend:
                        stitch_array.append(legend[stitch])
                    else:
                        stitch_array.append(stitch)
                        print(f"Error: Stitch {stitch} is not found in legend")

    return stitch_array


def print_chart(stitch_array: Set[str]) -> Image:
    """ Print a chart from a stitch array """

    # Set up the image
    cell_height = 50
    cell_width = 50
    chart_image = Image.new(
        "RGB", ((cell_width + 1) * len(stitch_array), cell_height), (200, 200, 200)
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)
    for i in range(1, len(stitch_array)):
        draw.line(
            ((cell_width + 1) * i, 0) + ((cell_width + 1) * i, cell_height), fill=128
        )
    return chart_image

    # draw symbol for each cell
    fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
    draw.text((10, 10), "HI", font=fnt, fill=(255, 255, 255, 255))


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


import math


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
