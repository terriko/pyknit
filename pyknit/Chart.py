# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.Chart: chart and pattern parsing functions
"""

import re
from PIL import Image, ImageDraw, ImageFont
from typing import List, Set

stitch_legend = {  # Default legend. Incomplete for now.
    "k": {
        "instruction": "knit",
        "symbol": " ",
        "width": 1,  
    },
    "kfb": {
        "instruction": "knit front and back",
        "symbol": "V",
        "width": 1,
    },
    "k2tog": {
        "instruction": "knit two together",
        "symbol": "/",
        "width": 1,
    },
    "yo": {
        "instruction": "yarn over",
        "symbol": "O",
        "width": 1
    },
    "p": {
        "instruction": "purl", 
        "symbol": ".",
        "width": 1,
    },
    "ssk": {
        "instruction": "slip slip knit", # left-leaning decrease 
        "symbol": "\\",
        "width": 1,
    },
}

class Stitch:
    """A class to represent a stitch. Optionally, a preferred legend can be passed in."""
    def __init__(self, stitch_name: str, legend: Set[str]=stitch_legend): 
        if stitch_name not in legend:
            raise KeyError(f"Stitch '{stitch_name}' not found in legend.")

        stitch_info = legend[stitch_name]

        self.instruction = stitch_info["instruction"]
        self.symbol = stitch_info["symbol"]
        self.width = stitch_info["width"]

    def __repr__(self):
        return f"'{self.symbol}'"

    def __str__(self):
        return f"{self.instruction}"

    def __eq__(self, other):
        if isinstance(other, Stitch):
            return self.__dict__ == other.__dict__
        return False
            

## Chart and pattern parsing functions


def parse_row(row: str, legend: Set[str]=stitch_legend) -> Set[str]:
    # I don't think a set is the right return type, order is important here
    """Parse a written set of knitting instructions and print an array of
    stitches using a legend.  This is a stand in for eventually printing a
    chart."""

    stitch_array = []
    for section in row.split(" "):

        patterns = [
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
                    stitch_array.append(Stitch(stitch, legend))

    return stitch_array


def parse_chart(chart_instructions:str, legend: Set[str]=stitch_legend) -> List[List[Stitch]]:
    return [parse_row(row) for row in chart_instructions.split("\n")]


def print_row(stitch_array: Set[str]) -> Image: 
    """ Print a chart from a stitch array """
    # TODO do a 2D chart
    # Set up the image
    cell_height = 50
    cell_width = 50
    chart_image = Image.new(
        "RGB", ((cell_width + 1) * sum(st.width for st in stitch_array), cell_height), (200, 200, 200)
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)

    # draw symbol for each cell
    fnt = ImageFont.truetype("cour.ttf", 40)
    position = 0
    for i, stitch in enumerate(stitch_array):

    # for i in range(1, len(stitch_array)):
        position = sum(st.width for st in stitch_array[:i+1]) * (cell_width + 1)
        draw.line(
            (position, 0) + (position, cell_height), fill=128
        )

    
        draw.text(
            (position - (stitch.width * cell_width)/2, cell_height/2),
            stitch.symbol, font=fnt,
            fill=(255, 255, 255, 255),
            align="center",
            anchor="mm"
        )
    return chart_image

def instruction_to_plot_order(input_array:str, vertical_order:str="bt", horizontal_order:str="rl"):
    # input_array = [list(row) for row in pattern.lstrip().rstrip().split("\n")]
    vertical_ordered = list(reversed(input_array)) if vertical_order == "bt" else input_array
    return_array = [list(reversed(row)) if horizontal_order == "rl" else row
        for row in vertical_ordered 
    ]
    return return_array


def plot_chart(stitch_array: List[List[str]], lr_direction:str="lr", tb_direction:str="tb") -> Image: 
    """ Print a chart from a stitch array """
    # TODO do a 2D chart
    # Set up the image
    cell_height = 50
    cell_width = 50

    num_rows = len(stitch_array)
    if num_rows <=0:
        raise ValueError("There must be at least one row in the pattern")
    
    longest_row_len = max([sum(st.width for st in row) for row in stitch_array])

    print(f"{num_rows} rows, {longest_row_len} sts wide at max")
    sts_to_plot = instruction_to_plot_order(stitch_array, tb_direction,lr_direction)

    chart_image = Image.new(
        "RGB", (cell_width * longest_row_len, cell_height*num_rows), (200, 200, 200)
    )

    # draw some gridlines
    draw = ImageDraw.Draw(chart_image)

    # draw symbol for each cell
    fnt = ImageFont.truetype("cour.ttf", 35)
    color_st_pattern = r"#[0-9a-fA-F]{6}"

    for st_y, row in enumerate(sts_to_plot):
        cur_y = st_y * cell_height
        cur_x = 0
        for st_x, stitch in enumerate(row):
        # for i in range(1, len(stitch_array)):
            stitch_coloured = re.match(color_st_pattern, stitch.symbol)
            stitch_color = stitch.symbol if stitch_coloured else "white"
            draw.rectangle(
                ((cur_x, cur_y), (cur_x+stitch.width*cell_width, cur_y+cell_height)),
                fill=stitch_color,
                outline="black"
            )
            if not stitch_coloured:
                draw.text(
                    (cur_x + (stitch.width * cell_width)/2, cur_y + cell_height/2),
                    stitch.symbol, font=fnt,
                    fill="blue",
                    align="center",
                    anchor="mm"
                )
            cur_x +=stitch.width*cell_width

    return chart_image
