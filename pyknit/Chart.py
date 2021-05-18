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
from typing import Set

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


def parse_written(row: str, legend: Set[str]=stitch_legend) -> Set[str]:
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
                    stitch_array.append(Stitch(stitch, legend))

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

    # draw symbol for each cell
    fnt = ImageFont.truetype("Courier New.ttf", 40)
    for i, stitch in enumerate(stitch_array):
        draw.text(
            ((cell_width + 1) * i, 3), stitch.symbol, font=fnt, fill=(255, 255, 255, 255)
        )
    return chart_image
