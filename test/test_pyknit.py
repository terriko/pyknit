#!python

import pytest
from pyknit import pyknit


def test1():
    stitchstring = "k1 p4 k1 p4 k kfb r ssk k2tog"
    legend = {
        "k": " ",
        "p": ".",
        "kfb": "\\/",
        "ssk": "\\",
        "k2tog": "k2tog",
    }
    expected = [
        " ",
        ".",
        ".",
        ".",
        ".",
        " ",
        ".",
        ".",
        ".",
        ".",
        " ",
        "\\/",
        "r",
        "\\",
        "k2tog",
    ]
    output_array = pyknit.parse_written(stitchstring, legend)
    assert output_array == expected


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
