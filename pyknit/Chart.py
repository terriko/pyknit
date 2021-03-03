#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.Chart: chart and pattern parsing functions
"""

import re
from PIL import Image, ImageDraw, ImageFont
from typing import Set


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
