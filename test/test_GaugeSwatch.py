# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python

import pytest
from pyknit import GaugeSwatch

@pytest.fixture
def swatch():
    return GaugeSwatch(row_count=18, row_measure=3.25, stitch_count=24, stitch_measure=4, units="in")

class TestGaugeSwatch:
    
    def test_row_gauge(self, swatch):
        assert swatch.row_gauge() == 18 / 3.25

    def test_stitch_gauge(self, swatch):
        assert swatch.stitch_gauge() == 24 / 4

    def test_measurement_to_stitches(self, swatch):
        assert swatch.measurement_to_stitches(5) == 30

    def test_measurement_to_rows(self, swatch):
        assert swatch.measurement_to_rows(11) == 61

    def test_rows_to_measurement(self, swatch):
        assert swatch.rows_to_measurement(10) == 10 / (18 / 3.25)

    def test_stitches_to_measurement(self, swatch):
        assert swatch.stitches_to_measurement(18) == 3