#!/usr/bin/env python3
from pyknit import pi_shawl


def test_pi_shawl_increase_rows():
    assert pi_shawl.pi_shawl_increase_rows(5, 5) == [2, 6, 13]
    assert pi_shawl.pi_shawl_increase_rows(50, 3) == [2, 6, 13, 26, 51, 100]
