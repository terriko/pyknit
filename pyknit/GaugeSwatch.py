# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.GaugeSwatch: Tools for measurement and gauge swatching
"""

import math
from typing import Set
from pydantic import BaseModel, PositiveInt, PositiveFloat, validate_arguments
from pydantic.typing import Literal


class GaugeSwatch(BaseModel):
    """Information from a gauge swatch"""
    row_count: PositiveInt
    row_measure: PositiveFloat
    stitch_count: PositiveInt
    stitch_measure: PositiveFloat
    units: Literal['cm', 'in']
    # TODO: add yardage/weight for calculations?

    def row_gauge(self) -> float:
        """ return rows per unit (e.g. cm, inch) number """
        return self.row_count / self.row_measure

    def stitch_gauge(self) -> float:
        """ return stitches per unit (e.g. cm, inch) number """
        return self.stitch_count / self.stitch_measure

    @validate_arguments
    def measurement_to_stitches(self, measurement: PositiveFloat) -> int:
        """
        Given a measurement, how many stiches would we need?
        Round to closest stitch.
        """
        return round(measurement * self.stitch_gauge())

    @validate_arguments
    def measurement_to_rows(self, measurement: PositiveFloat) -> int:
        """
        Given a measurement, how many rows would we need?
        Round to closest number of rows."""
        return round(measurement * self.row_gauge())

    @validate_arguments
    def rows_to_measurement(self, rows: PositiveInt) -> float:
        """ figure out how long a number of rows will be """
        return rows / self.row_gauge()

    @validate_arguments
    def stitches_to_measurement(self, stitches: PositiveInt) -> float:
        """ figure out how wide a number of stitches will be """
        return stitches / self.stitch_gauge()


# Gauge and stich count related functions


def stitch_count(stitch_array: Set[str], legend: Set[str]) -> int:
    if legend:
        # FIXME: Do calculations per stitch
        return len(stitch_array)

    # otherwise, assume every stitch has width=1
