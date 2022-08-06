# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

import argparse
import logging

from pyknit import VERSION, GaugeSwatch


def main():
    # set up the logger
    logger = logging.getLogger(__package__)
    logging.basicConfig(level=logging.INFO, format="%(message)s")

    print(f"{VERSION}")
    desc = """
    This package is intended for use as a library inside jupyter notebook,
    but has some basic gauge calculations available on the command line.
    Use --convert to convert from one gauge to another.
    """
    logger.warning(desc)
    parser = argparse.ArgumentParser(prog="pyknit", description=desc)

    # Goal: measurement conversions from one gauge to another
    # e.g.
    #  - pattern gauge was 8 stitches / inch.
    #  - my actual gauge was 7.5 stitches / inch
    #  - Therefore, a 18 inch sleeve in the pattern will now be 19.2 inches

    conversion_options_group = parser.add_argument_group(
        "Conversion Options",
    )
    conversion_options_group.add_argument(
        "--convert",
        help="Convert from one gauge to another. Specify row or stitch to indicate which direction of measurement you need to convert.",
        choices=["row", "stitch"],
        type=str,
        action="store",
    )

    # Set details for original gauge (often this will be pattern gague)
    original_gauge_group = parser.add_argument_group("Original Gauge Details")
    original_gauge_group.add_argument(
        "--original-gauge-row",
        "-ogr",
        help="Original gauge (typically from the pattern) in rows/inch",
        action="store",
        type=float,
        default=None,
    )
    original_gauge_group.add_argument(
        "--original-gauge-stitch",
        "-ogs",
        help="Original gauge (typically from the pattern) in stitches/inch",
        type=float,
        action="store",
        default=None,
    )
    original_gauge_group.add_argument(
        "--original-gauge-measurement",
        "-ogm",
        help="Original gauge swatch measurement (numbers only)",
        type=float,
        action="store",
        default=1,
    )
    original_gauge_group.add_argument(
        "--original-gauge-unit",
        "-ogu",
        help="Original gauge units (in or cm)",
        type=str,
        action="store",
        default="in",
    )

    # Arguments for my gauge (measured from your own swatch)
    new_gauge_group = parser.add_argument_group("New Gauge Details")
    new_gauge_group.add_argument(
        "--new-gauge-row",
        "-ngr",
        help="New gauge (typically from your swatch) in rows/inch",
        type=float,
        action="store",
        default=None,
    )
    new_gauge_group.add_argument(
        "--new-gauge-stitch",
        "-ngs",
        help="Original gauge (typically from your swatch) in stitches/inch",
        type=float,
        action="store",
        default=None,
    )
    new_gauge_group.add_argument(
        "--new-gauge-measurement",
        "-ngm",
        help="New gauge swatch measurement (numbers only)",
        type=float,
        action="store",
        default=1,
    )
    new_gauge_group.add_argument(
        "--new-gauge-unit",
        "-ngu",
        help="New gauge units (in or cm)",
        type=str,
        action="store",
        default="in",
    )

    parser.add_argument(
        "--original-measurement",
        help="Original measurement (typically from the pattern) that you wish to convert",
        action="store",
        type=float,
    )

    args = parser.parse_args()

    if not args.convert:
        parser.print_usage()
        exit()

    if args.convert == "row":
        # If we're converting for rows, we only neeed row-related measurements
        # Make sure we have what we need or request it as input.
        logger.info("Converting row gauge...")
        if not args.original_gauge_row:
            original_gauge_row = input(
                f"Please enter a valid original gauge (row/{args.original_gauge_unit}): "
            )
        else:
            original_gauge_row = args.original_gauge_row

        if not args.new_gauge_row:
            new_gauge_row = input(
                f"Please enter a valid new gauge (row/{args.new_gauge_unit}): "
            )
        else:
            new_gauge_row = args.new_gauge_row

        if not args.original_measurement:
            original_measurement = input(
                f"Please enter the measurement you want to convert ({args.original_gauge_unit}): "
            )
        else:
            original_measurement = args.original_measurement

        # Show what numbers we're using
        logger.info("")
        logger.info(
            f"Original gauge: {original_gauge_row} rows/{args.original_gauge_unit}"
        )
        logger.info(f"New gauge: {new_gauge_row} rows/{args.new_gauge_unit}")
        logger.info(
            f"Original pattern measurement: {original_measurement} {args.original_gauge_unit}"
        )

        # We only need the row info so we're setting the rest to 1 for convenience.
        # FIXME: Need to add something to convert cm/in if the gagues are different
        original_gauge = GaugeSwatch(
            row_count=original_gauge_row,
            stitch_count=1,
            row_measure=1,
            stitch_measure=1,
            units=args.original_gauge_unit,
        )
        new_gauge = GaugeSwatch(
            row_count=new_gauge_row,
            stitch_count=1,
            row_measure=1,
            stitch_measure=1,
            units=args.new_gauge_unit,
        )
        original_gauge_rows = original_gauge.measurement_to_rows(original_measurement)
        new_measurement = new_gauge.rows_to_measurement(original_gauge_rows)
        logger.info(
            f"My calculated measurement: {new_measurement} {args.original_gauge_unit}"
        )
        logger.info("")

    elif args.convert == "stitch":
        # If we're converting for rows, we only neeed stitch-related measurements
        # Make sure we have what we need or request it as input.

        logger.info("Converting stitch gauge...")
        if not args.original_gauge_stitch:
            original_gauge_stitch = input(
                f"Please enter a valid original gauge (stitch/{args.original_gauge_unit}): "
            )
        else:
            original_gauge_stitch = args.original_gauge_stitch

        if not args.new_gauge_stitch:
            new_gauge_stitch = input(
                f"Please enter a valid new gauge (stitch/{args.new_gauge_unit}): "
            )
        else:
            new_gauge_stitch = args.new_gauge_stitch

        if not args.original_measurement:
            original_measurement = input(
                f"Please enter the measurement you want to convert ({args.original_gauge_unit}): "
            )
        else:
            original_measurement = args.original_measurement

        # Show what numbers we're using
        logger.info("")
        logger.info(
            f"Original gauge: {original_gauge_stitch} stitchs/{args.original_gauge_unit}"
        )
        logger.info(f"New gauge: {new_gauge_stitch} stitchs/{args.new_gauge_unit}")
        logger.info(
            f"Original pattern measurement: {original_measurement} {args.original_gauge_unit}"
        )

        # We only need the stitch info so we're setting the rest to 1 for convenience.
        # FIXME: Need to add something to convert cm/in if the gagues are different
        original_gauge = GaugeSwatch(
            stitch_count=original_gauge_stitch,
            row_count=1,
            row_measure=1,
            stitch_measure=1,
            units=args.original_gauge_unit,
        )
        new_gauge = GaugeSwatch(
            stitch_count=new_gauge_stitch,
            row_count=1,
            row_measure=1,
            stitch_measure=1,
            units=args.new_gauge_unit,
        )
        original_gauge_stitches = original_gauge.measurement_to_stitches(
            original_measurement
        )
        new_measurement = new_gauge.stitches_to_measurement(original_gauge_stitches)
        logger.info(
            f"My calculated measurement: {new_measurement} {args.original_gauge_unit}"
        )
        logger.info("")

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
