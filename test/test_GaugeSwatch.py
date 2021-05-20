# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python

import pytest
import pyknit
from pyknit.GaugeSwatch import GaugeSwatch
import math
from typing import Set


def test_init():
    gs = GaugeSwatch(row_count=18, row_measure=3.25, stitch_count=24, stitch_measure=4, units="in")
    assert isinstance(gs, GaugeSwatch)
    assert gs.row_count == 18
    assert gs.row_measure == 3.25
    assert gs.stitch_count == 24
    assert gs.stitch_measure == 4
    assert gs.units == "in"

@pytest.fixture
def example_gauge_swatches():
    gs_good_1 = GaugeSwatch(row_count=22, row_measure=3.75, stitch_count=18, stitch_measure=4, units="in")
    gs_good_2 = GaugeSwatch(row_count=18, row_measure=3.25, stitch_count=24, stitch_measure=4, units="in")
    return [gs_good_1, gs_good_2]

def test_row_gauge(example_gauge_swatches):
    expected = [22/3.75, 18/3.25]
    computed = [gs.row_gauge() for gs in example_gauge_swatches]
    assert computed == expected

def test_stitch_gauge(example_gauge_swatches):
    expected = [18/4, 24/4]
    computed = [gs.stitch_gauge() for gs in example_gauge_swatches]
    assert computed == expected
