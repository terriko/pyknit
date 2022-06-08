# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

import argparse
import logging

from pyknit import VERSION, GaugeSwatch


def main():
    # set up the logger
    logger = logging.getLogger(__package__)
    logger.setLevel(logging.INFO)

    print(f"{VERSION}")
    desc = """
    This package is intended for use as a library inside jupyter notebook,
    but has some basic gauge calculations available on the command line.
    """
    logger.warning(desc)
    parser = argparse.ArgumentParser(prog="pyknit", description=desc)

    # Goal: measurement conversions from one gauge to another
    # e.g.
    #  - pattern gauge was 8 stitches / inch.
    #  - my actual gauge was 7.5 stitches / inch
    #  - Therefore, a 18 inch sleeve in the pattern will now be 19.2 inches
    parser.add_argument(
        "--pattern-gauge-row",
        help="Original gauge (typically from the pattern) in rows/inch",
        action="store",
    )

    parser.add_argument(
        "--my-gauge-row",
        help="My actual measured gauge (from a swatch) in rows/inch",
        action="store",
    )

    parser.add_argument(
        "--pattern-measurement",
        help="Original measurement (typically from the pattern) that you wish to convert",
        action="store",
    )

    args = parser.parse_args()
    print(args)

    # logger.info(f"Pattern gauge: {args['pattern_gauge_row']} rows/inch")
    # logger.info(f"My actual gauge: {my_gauge_row} rows/inch")
    # logger.info(f"Original pattern measurement: {pattern_measurement} inches")
    pattern_gauge = GaugeSwatch(
        row_count=args.pattern_gauge_row,
        stitch_count=1,
        row_measure=1,
        stitch_measure=1,
        units="in",
    )
    my_gauge = GaugeSwatch(
        row_count=args.my_gauge_row,
        stitch_count=1,
        row_measure=1,
        stitch_measure=1,
        units="in",
    )
    pattern_rows = pattern_gauge.measurement_to_rows(args.pattern_measurement)
    my_measurement = my_gauge.rows_to_measurement(pattern_rows)
    logger.warning(f"My calculated measurement: {my_measurement}")

    # legend = {
    #    "k": "k",
    #    "p": "p",
    #    "kfb": "kfb",
    #    "ssk": "ssk",
    #    "k2tog": "k2tog",
    #    "p2tog": "p2tog",
    # }

    # print(parse_written(args.instruction_row, legend))


if __name__ == "__main__":
    main()
