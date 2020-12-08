#!python

import re


def parse_written(row, legend):
    """Parse a written set of knitting instructions and print an array of stitches using a legend.
    This is a stand in for eventually printing a chart."""

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
