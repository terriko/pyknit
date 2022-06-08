# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.Chart: chart and pattern parsing functions
"""

import os
import os.path
import re
from posixpath import relpath
from typing import Dict, List, Sequence, Set

from PIL import Image, ImageDraw, ImageFont


class Stitch:
    """A class to represent a stitch. Optionally, a preferred legend can be passed in."""

    def __init__(self, instruction: str, symbol: str, width: int):
        self.instruction = instruction
        self.symbol = symbol
        self.width = width

    def __repr__(self):
        return f"'{self.symbol}'"

    def __str__(self):
        return f"{self.instruction}"

    def __eq__(self, other):
        if isinstance(other, Stitch):
            return self.__dict__ == other.__dict__
        return False


Legend = Dict[str, Stitch]
PatternRow = List[Stitch]
Pattern = List[PatternRow]

symbol_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "symbols",
)

stitch_legend = {  # Default legend. Incomplete for now.
    "k": Stitch(instruction="knit", symbol=" ", width=1),
    "kfb": Stitch(
        instruction="knit front and back",
        symbol="V",
        width=1,
    ),
    "k2tog": Stitch(
        instruction="knit two together",
        symbol="/",
        width=1,
    ),
    "yo": Stitch(instruction="yarn over", symbol="O", width=1),
    "p": Stitch(
        instruction="purl",
        symbol=".",
        width=1,
    ),
    "ssk": Stitch(
        instruction="slip slip knit",  # left-leaning decrease
        symbol="\\",
        width=1,
    ),
    "C1-1L": Stitch(
        instruction="sl 1st onto cn, with cn in front, k1, k1 from cn",
        symbol=os.path.join(symbol_dir, "C1-1L.png"),
        width=2,
    ),
    "C1-1R": Stitch(
        instruction="sl 1st onto cn, with cn in back, k1, k1 from cn",
        symbol=os.path.join(symbol_dir, "C1-1R.png"),
        width=2,
    ),
    "C2-1L": Stitch(
        instruction="sl 2st onto cn, with cn in front, k1, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-1L.png"),
        width=3,
    ),
    "C2-1R": Stitch(
        instruction="sl 2st onto cn, with cn in back, k1, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-1R.png"),
        width=3,
    ),
    "C2-1PL": Stitch(
        instruction="sl 2st onto cn, with cn in front, p1, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-1PL.png"),
        width=3,
    ),
    "C2-1PR": Stitch(
        instruction="sl 2st onto cn, with cn in back, p1, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-1PR.png"),
        width=3,
    ),
    "C2-2L": Stitch(
        instruction="sl 2st onto cn, with cn in front, k2, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-2L.png"),
        width=4,
    ),
    "C2-2R": Stitch(
        instruction="sl 2st onto cn, with cn in back, k2, k2 from cn",
        symbol=os.path.join(symbol_dir, "C2-2R.png"),
        width=4,
    ),
}
## Chart and pattern parsing functions


def parse_row(row: str, legend: Legend = stitch_legend) -> List[str]:
    # I don't think a set is the right return type, order is important here
    """Parse a written set of knitting instructions and print an array of
    stitches using a legend.  This is a stand in for eventually printing a
    chart."""

    stitch_array = []
    for section in row.split(" "):

        patterns = [
            r"(C\d-\dP?[F|B|L|R])([0-9]*)",  # cables
            r"([A-Za-z]+[0-9]+[A-Za-z]+)([0-9]*)",  # things like k2tog or m1l
            r"([A-Za-z]+)([0-9]*)",  # things like p4
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
                    stitch_array.append(legend[stitch])

    return stitch_array


def parse_chart(chart_instructions: str, legend: Legend = stitch_legend) -> Pattern:
    return [parse_row(row, legend) for row in chart_instructions.split("\n")]


def print_row(stitch_array: PatternRow) -> Image:
    """Print a chart from a stitch array"""
    # Set up the image
    cell_height = 50
    cell_width = 50
    chart_image = Image.new(
        "RGB",
        ((cell_width + 1) * sum(st.width for st in stitch_array), cell_height),
        (200, 200, 200),
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)

    # draw symbol for each cell
    fnt = ImageFont.truetype("cour.ttf", 40)
    position = 0
    for i, stitch in enumerate(stitch_array):

        # for i in range(1, len(stitch_array)):
        position = sum(st.width for st in stitch_array[: i + 1]) * (cell_width + 1)
        draw.line((position, 0) + (position, cell_height), fill=128)

        draw.text(
            (position - (stitch.width * cell_width) / 2, cell_height / 2),
            stitch.symbol,
            font=fnt,
            fill=(255, 255, 255, 255),
            align="center",
            anchor="mm",
        )
    return chart_image


def instruction_to_plot_order(
    input_array: Pattern, vertical_order: str = "bt", horizontal_order: str = "rl"
) -> Pattern:
    # input_array = [list(row) for row in pattern.lstrip().rstrip().split("\n")]
    vertical_ordered = (
        list(reversed(input_array)) if vertical_order == "bt" else input_array
    )
    return_array = [
        list(reversed(row)) if horizontal_order == "rl" else row
        for row in vertical_ordered
    ]
    return return_array


def plot_chart(
    stitch_array: Pattern, lr_direction: str = "lr", tb_direction: str = "tb"
) -> Image:
    """Print a chart from a stitch array"""

    # Set up the image
    cell_height = 50
    cell_width = 50

    num_rows = len(stitch_array) if type(stitch_array[0] == list) else 1
    if num_rows <= 0:
        raise ValueError("There must be at least one row in the pattern")
    elif num_rows == 1:
        stitch_array = [
            stitch_array
        ]  # put a single row into a containing list to make the 2D loop work

    longest_row_len = max([sum(st.width for st in row) for row in stitch_array])

    print(f"{num_rows} rows, {longest_row_len} sts wide at max")
    pattern_to_plot = instruction_to_plot_order(
        stitch_array, tb_direction, lr_direction
    )

    # Set up canvas with room for all stitches plus numbers
    chart_image = Image.new(
        "RGB",
        (cell_width * (longest_row_len + 1), cell_height * (num_rows + 1)),
        (200, 200, 200),
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)

    # draw symbol for each cell
    fnt = ImageFont.truetype("cour.ttf", 35)
    color_st_pattern = r"#[0-9a-fA-F]{6}"

    for st_y, row in enumerate(pattern_to_plot):
        cur_y = (st_y + (1 if tb_direction == "tb" else 0)) * cell_height
        cur_x = 0 if lr_direction == "rl" else cell_width
        for st_x, stitch in enumerate(row):
            # for i in range(1, len(stitch_array)):
            stitch_coloured = re.match(color_st_pattern, stitch.symbol)
            stitch_graphic = stitch.symbol.endswith(".png")

            if (
                stitch_graphic
            ):  # this is really ugly, fix path to symbols as part of the symbol name?
                with Image.open(stitch.symbol) as sym:
                    chart_image.paste(sym, (cur_x, cur_y))

            else:
                stitch_color = stitch.symbol if stitch_coloured else "white"
                draw.rectangle(
                    (
                        (cur_x, cur_y),
                        (cur_x + stitch.width * cell_width, cur_y + cell_height),
                    ),
                    fill=stitch_color,
                    outline="black",
                )
                if not stitch_coloured:
                    draw.text(
                        (
                            cur_x + (stitch.width * cell_width) / 2,
                            cur_y + cell_height / 2,
                        ),
                        stitch.symbol,
                        font=fnt,
                        fill="blue",
                        align="center",
                        anchor="mm",
                    )
            cur_x += stitch.width * cell_width
    # Row and column numbers
    row_x = (
        3 * cell_width // 2
        if lr_direction == "lr"
        else chart_image.width - 3 * cell_width // 2
    )
    row_y = (
        cell_height // 2
        if tb_direction == "tb"
        else chart_image.height - cell_height // 2
    )
    for i in range(1, longest_row_len + 1):
        draw.text(
            (row_x, row_y),
            str(i),
            fill="black",
            font=fnt,
            align="center",
            anchor="mm",
        )
        row_x = row_x + cell_width * (1 if lr_direction == "lr" else -1)

    col_x = (
        cell_width // 2 if lr_direction == "lr" else chart_image.width - cell_width // 2
    )
    col_y = (
        3 * cell_height // 2
        if tb_direction == "tb"
        else chart_image.height - 3 * cell_height // 2
    )
    for j in range(1, num_rows + 1):
        draw.text(
            (col_x, col_y),
            str(j),
            fill="black",
            font=fnt,
            align="center",
            anchor="mm",
        )
        col_y = col_y + cell_height * (1 if tb_direction == "tb" else -1)

    return chart_image
