#!python

import argparse
import math
import re
from PIL import Image, ImageDraw, ImageFont


def parse_written(row, legend):
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
                # only match one pattern per stitch so k2tog doesn't also get parsed as k2
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


def print_chart(stitch_array):
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


def increase_evenly(starting_count, increase_number, in_the_round=False):
    """ A function to figure out even spacing for increases """

    if in_the_round == False:
        # to avoid increases at start/end of row in a flat piece, add 1
        increase_spacing = increase_number + 1
    else:
        increase_spacing = increase_number

    interval = math.floor(starting_count / (increase_spacing))
    remainder = starting_count % increase_spacing

    # TODO: spread out the remainder nicely.  For now, we're tacking it on the enda
    # TODO: Honestly, I think something is wrong in the math in the round.
    print(f"increase {interval} stitches with remainder {remainder}")

    # This nested f thing is probably not the most readable
    print(f'{(f"k{interval}, m1, ")*increase_number}k{interval+remainder}')


def decrease_evenly(starting_count, decrease_number, in_the_round=False):
    """ A function to figure out spacing for decreases """


def sleeve_decreases(number_of_rows, starting_count, ending_count, decrease_per_row=2):
    """ A function to figure out a nice even sleeve decrease. """


def row_count(stitch_array, legend):
    if legend:
        # Do calculations per stitch
        return len(stitch_array)

    # otherwise, assume every stitch has width=1
    return len(stitch_array)


def main():
    print("PyKnit 0.0.1")
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
