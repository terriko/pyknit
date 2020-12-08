#!python

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
