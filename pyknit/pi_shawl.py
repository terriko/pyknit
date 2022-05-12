#!/usr/bin/env python3
import argparse
from logging.config import dictConfig

from pyknit import logging_config_dict


def total_rounds_for_pi_shawl(desired_radius: float, round_gauge: float) -> int:
    """Returns number of rounds necessary to create a pi shawl of given radius"""
    return round(desired_radius * round_gauge)


def pi_shawl_increase_rows(desired_radius: float, round_gauge: float) -> str:
    "returns a list with the number of round at which to double the stitches"
    num_rounds_for_pi_shawl = total_rounds_for_pi_shawl(desired_radius, round_gauge)
    num_of_rounds_before_increase_step = 3
    increase_rows = [2]  # increase on first round after cast-on
    num_round = 2
    while num_round <= num_rounds_for_pi_shawl:
        num_rounds_since_last_increase_row = num_round - increase_rows[-1]
        if num_rounds_since_last_increase_row == num_of_rounds_before_increase_step + 1:
            increase_rows.append(num_round)
            num_of_rounds_before_increase_step = num_of_rounds_before_increase_step * 2
        num_round += 1
    return increase_rows


def main():
    parser = argparse.ArgumentParser(description="Pi shawl calculations")
    parser.add_argument("desired_radius", type=float, help="Radius of your pi shawl")
    parser.add_argument("round_gauge", type=float, help="Rows per measurement unit")
    args = parser.parse_args()
    print(pi_shawl_increase_rows(args.desired_radius, args.round_gauge))


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
