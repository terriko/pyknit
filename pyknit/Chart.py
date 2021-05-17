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

stitch_legend = {
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
    # "p": ".",
    # "ssk": "\\",
}

class Stitch:
    def __init__(self, stitch_name):
        if stitch_name not in stitch_legend:
            raise KeyError(f"Stitch '{stitch_name}' not found.")

        stitch_info = stitch_legend[stitch_name]

        self.instruction = stitch_info["instruction"]
        self.symbol = stitch_info["symbol"]
        self.width = stitch_info["width"]

    def __repr__(self):
        return f"{self.instruction}"

        

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

    # draw symbol for each cell
    fnt = ImageFont.truetype("Courier New.ttf", 40)
    for i, stitch in enumerate(stitch_array):
        draw.text(
            ((cell_width + 1) * i, 3), stitch, font=fnt, fill=(255, 255, 255, 255)
        )
    return chart_image
