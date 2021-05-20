# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python

import pytest
import pyknit


def test_parse_written():
    """Test parse_written's ability to convert a string of stitches 
    into an array of Stitch objects. The built-in stitch_legend dict is used
    as the legend."""
    stitchstring = "k1 p4 k1 p4 k kfb yo ssk k2tog"
    expected = [
        pyknit.Chart.Stitch("k"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("k"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("p"),
        pyknit.Chart.Stitch("k"),
        pyknit.Chart.Stitch("kfb"),
        pyknit.Chart.Stitch("yo"),
        pyknit.Chart.Stitch("ssk"),
        pyknit.Chart.Stitch("k2tog"),
    ]
    output_array = pyknit.Chart.parse_written(stitchstring, pyknit.Chart.stitch_legend)
    assert output_array == expected

def test_Stitch_unknown_stitch():
    """A stitch in the string that is not found in the legend should raise
    a KeyError: 'Stitch not found in legend.'"""
    with pytest.raises(KeyError):
        bad_stitch = pyknit.Chart.Stitch("r")

@pytest.mark.parametrize(
    ("starting_count", "increase_number", "in_the_round", "expected"),
    [
        (11, 3, False, "k2, m1, [k3, m1] * 2 times, k3"),
        (10, 7, False, "[k1, m1] * 6 times, k2, m1, k2"),
        (11, 3, True, "k3, m1, [k4, m1] * 2 times"),
        (20, 5, True, "[k4, m1] * 5 times"),
        (21, 5, True, "[k4, m1] * 4 times, k5, m1"),
        (19, 5, True, "k3, m1, [k4, m1] * 4 times"),
    ],
)
def test_increase_evenly(starting_count, increase_number, in_the_round, expected):
    assert (
        pyknit.increase_evenly(starting_count, increase_number, in_the_round)
        == expected
    )
