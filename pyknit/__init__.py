# Copyright (C) 2022 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more
"""

import logging
import math
from logging.config import dictConfig
from typing import Set

from pydantic import PositiveInt, validate_arguments

from .Chart import *
from .GaugeSwatch import *
from .Hat import *

logging_config_dict = dict(
    version=1,
    formatters={"simple": {"format": """%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s | %(message)s"""}},
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)

VERSION = "pyKnit 0.0.6"

# Increase and decrease functions

@validate_arguments
def increase_evenly(
    starting_count: PositiveInt, increase_number: PositiveInt, in_the_round: bool = False
) -> str:
    """ A function to figure out even spacing for increases """

    if increase_number > starting_count:
        logging.error(
            f"Error: Increase number ({increase_number}) is bigger than the starting count ({starting_count})")
        raise ValueError

    if not in_the_round:
        # It's increase+1 so that you don't have increases at either
        # the start or end of a row
        increase_spacing = increase_number + 1
    else:
        increase_spacing = increase_number

    interval = math.floor(starting_count / (increase_spacing))
    remainder = starting_count % increase_spacing

    # first set of increases
    if increase_spacing - remainder > 1:
        instruction_string = f"[k{interval}, m1] * {increase_spacing-remainder} times"
    else:
        instruction_string = f"k{interval}, m1"

    # second set of increases (if needed)
    if remainder > 0:
        if not in_the_round:
            if remainder - 1 > 1:
                instruction_string += (
                    f", [k{interval+1}, m1] * {remainder-1} times, k{interval+1}"
                )
            else:
                instruction_string += f", k{interval+1}, m1, k{interval+1}"
        else:
            if remainder > 1:
                instruction_string += f", [k{interval+1}, m1] * {remainder} times"
            else:
                instruction_string += f", k{interval+1}, m1"

    # if we still need a selvage, add that
    else:
        if not in_the_round:
            instruction_string += f", k{interval}"

    return instruction_string



def decreaseEvenlyRound(stCount, decreaseSts):
    decreasePattern = '['
    leftOver = stCount % decreaseSts
    if leftOver == 0:
        k = (stCount / decreaseSts) - 2
        times = decreaseSts
        if k != 0:
            decreasePattern += 'k' + str(int(k)) + ', '
        decreasePattern += 'k2tog] * ' + str(int(times))
        if times == 1:
            decreasePattern += ' time'
        else:
            decreasePattern += ' times'
    else:
        k = math.floor(stCount / decreaseSts) - 2
        kHigher = k + 1
        higherTimes = stCount % decreaseSts
        times = decreaseSts - higherTimes
        leftOver = stCount - (k + 2) * times - (kHigher + 2) * higherTimes
        kString = 'k2tog' if k == 0 else 'k' + str(k) + ', k2tog'
        kHigherString = 'k2tog' if kHigher == 0 else 'k' + str(int(kHigher)) + ', k2tog'
        if (times % 2 == 0):
            times = times / 2
            timesString = kString if times == 1 else ('[' + kString + '] * ' + str(int(times)) + ' times')
            higherTimesString = kHigherString if higherTimes == 1 else (
                        '[' + kHigherString + '] * ' + str(int(higherTimes)) + ' times')
            decreasePattern = timesString + ', ' + higherTimesString + ', ' + timesString + ''
        elif (higherTimes % 2 == 0):
            higherTimes = higherTimes / 2
            timesString = kString if times == 1 else ('[' + kString + '] * ' + str(int(times)) + ' times')
            higherTimesString = kHigherString if higherTimes == 1 else (
                        '[' + kHigherString + '] * ' + str(int(higherTimes)) + ' times')
            decreasePattern = higherTimesString + ', ' + timesString + ', ' + higherTimesString + ''
        else:
            higherTimes = math.ceil(higherTimes / 2)
            timesString = kString if times == 1 else ('[' + kString + '] ' + times + ' times, ')
            higherTimesString = kHigherString if higherTimes == 1 else (
                        '[' + kHigherString + '] ' + str(int(higherTimes)) + ' times')
            decreasePattern = higherTimesString + ', ' + timesString
            higherTimes += -1
            if (higherTimes != 0):
                decreasePattern += ''
    return decreasePattern


def decreaseEvenlyFlat(stCount, decreaseSts):
    decreasePattern = ''
    leftOver = stCount % decreaseSts
    if leftOver == 0:
        k = (stCount / decreaseSts) - 2
        kFirst = math.ceil(k / 2)
        kSecond = k - kFirst
        times = decreaseSts
        if kFirst != 0:
            times = times - 1
            decreasePattern += 'k' + str(int(kFirst)) + ', '
        if k != 0:
            decreasePattern += '[k2tog, k' + str(int(k)) + ']'
        else:
            decreasePattern += '[k2tog] '
        if times > 1:
            decreasePattern += ' * ' + str(int(times)) + ' times'
        if kSecond != 0:
            decreasePattern += ', k2tog, k' + str(int(kSecond))
        decreasePattern += ''

    else:
        k = math.floor(stCount / decreaseSts) - 2
        kHigher = k + 1
        higherTimes = stCount % decreaseSts
        times = decreaseSts - higherTimes
        leftOver = stCount - (k + 2) * times - (kHigher + 2) * higherTimes
        kString = 'k2tog, k' + str(int(k)) if k != 0 else 'k2tog'
        kHigherString = 'k2tog, k' + str(int(kHigher)) if kHigher != 0 else 'k2tog'

        if times % 2 == 0:
            times = times / 2
            higherTimes = higherTimes - 1
            higherTimesString = ''
            if higherTimes > 0:
                higherTimesString = ', ' + kHigherString if higherTimes == 1 else (
                            ', [' + kHigherString + '] *' + str(int(higherTimes)) + ' times')
            timesString = ', ' + kString if times == 1 else (', [' + kString + '] * ' + str(int(times)) + ' times')
            balancedStrFirst = 'k' + str(int(math.ceil(kHigher / 2))) if math.ceil(kHigher / 2) != 0 else ''
            balancedStrLast = ', k2tog k' + str(int(kHigher - math.ceil(kHigher / 2))) + '' if (kHigher - math.ceil(
                kHigher / 2)) != 0 else ''
            decreasePattern = balancedStrFirst + timesString + higherTimesString + timesString + balancedStrLast
        elif higherTimes % 2 == 0:
            higherTimes = higherTimes / 2
            times = times - 1
            timesString = ''
            if (times > 0):
                timesString = kString if times == 1 else ('[' + kString + '] * ' + times + ' times')
            higherTimesString = kHigherString if higherTimes == 1 else (
                        '[' + kHigherString + '] * ' + str(int(higherTimes)) + ' times')
            balancedStrFirst = 'k' + str(int(math.ceil(k / 2))) + ', ' if math.ceil(k / 2) != 0 else ''
            balancedStrLast = ', k2tog k' + str(int(k - math.ceil(k / 2))) + '' if (k - math.ceil(
                k / 2)) != 0 else ', k2tog'
            decreasePattern = balancedStrFirst + higherTimesString + timesString + ', ' + higherTimesString + balancedStrLast


        else:
            higherTimes = math.ceil(higherTimes / 2)
            higherTimesString = ''
            if (higherTimes > 0):
                higherTimesString = kHigherString if higherTimes == 1 else (
                            '[' + kHigherString + '] * ' + str(int(higherTimes - 1)) + ' times, ')
            timesString = kString if times == 1 else ('[' + kString + '] * ' + times + ' times, ')
            balancedStrFirst = 'k' + str(int(math.ceil(kHigher / 2))) + ', ' if math.ceil(kHigher / 2) != 0 else ''
            balancedStrLast = ', k2tog k' + str(int(kHigher - math.ceil(kHigher / 2))) + '' if (kHigher - math.ceil(
                kHigher / 2)) != 0 else ', k2tog'
            decreasePattern = balancedStrFirst + higherTimesString + timesString

            higherTimes += -1

            if (higherTimes != 0):
                higherTimesString = kHigherString if higherTimes == 1 else (
                            '[' + kHigherString + '] * ' + str(int(higherTimes)) + ' times')
                decreasePattern += higherTimesString
            decreasePattern += balancedStrLast
    return decreasePattern


def decrease_evenly(
        starting_count: PositiveInt, decrease_number: PositiveInt, in_the_round: bool = False
):
    """ A function to figure out spacing for decreases """
    if starting_count < 2:
        msg = f"You need to have at least 2 stitches; starting_count={starting_count}"
        logging.error(msg)
        raise ValueError
    if decrease_number < 2:
        msg = f"the amount of decrease needs to be at least 2; decrease_number={decrease_number}."
        logging.error(msg)
        raise ValueError
    if decrease_number > starting_count / 2:
        msg = f"the amount of decrease needs to be less than half of starting_count; decrease_number={decrease_number} > starting_count/2={starting_count / 2}"
        logging.error(msg)
        raise ValueError
    if decrease_number > starting_count:
        msg = f"Error: Decrease number ({decrease_number}) is bigger than the starting count ({starting_count})"
        logging.error(msg)
        raise ValueError

    if in_the_round:
        result = decreaseEvenlyRound(starting_count, decrease_number)
    else:
        result = decreaseEvenlyFlat(starting_count, decrease_number)
    return result


def sleeve_decreases(
    number_of_rows: PositiveInt,
    starting_count: PositiveInt,
    ending_count: PositiveInt,
    decrease_per_row: PositiveInt = 2,
) -> str:
    """ A function to figure out a nice even sleeve decrease. """

    # TODO: This function is going to be pretty similar to the decrease_evenly()
    # function.  We may want to combine them later.

    if starting_count < ending_count:
        logging.error(
            f"Error: No decreases needed, {starting_count} is already smaller than {ending_count}"
        )
        raise ValueError
    elif starting_count == ending_count:
        logging.error(
            f"Error: No decreases needed, the starting count is the same as the ending count"
        )
        raise ValueError

    # How many times are we doing the decrease row?
    number_of_decrease_rows = math.floor(
        (starting_count - ending_count) / decrease_per_row
    )
    if ((starting_count - ending_count) % decrease_per_row) > 0:
        # TODO: we could probably do this math for people if we wanted
        logging.warning(
            f"Warning: desired decrease doesn't work exactly with a {decrease_per_row} decrease"
        )
        logging.warning(
            "Printing the closest alternative but you'll need to add decreases at the end"
        )

    # divide up the number of rows.
    # This gives you a decrease on the first row but padding after the last
    # TODO: make an option for padding both sides, padding neither?

    interval = math.floor(
        (number_of_rows - number_of_decrease_rows) / number_of_decrease_rows
    )
    remainder = (number_of_rows - number_of_decrease_rows) % number_of_decrease_rows

    # If we had any remainder, pad out the early decreases
    instruction_string = ""
    if remainder > 0:
        instruction_string += (
            f"[decrease row, do {interval+1} rows in pattern] * {remainder} times, "
        )
    instruction_string += f"[decrease row, do {interval} rows in pattern] * {number_of_decrease_rows - remainder} times"

    return instruction_string


def raglan_increases(
    neck_stitches: PositiveInt,
    arm_stitches: PositiveInt,
    bust_stitches: PositiveInt,
    neck_to_bust_rows: PositiveInt,
    increase_per_increase_row: PositiveInt = 8,
    armpit_stitches: PositiveInt = 4,
) -> str:
    """Tool for adjusting raglan sweaters to increase arm size or bust size.

    For a standard raglan, you increase along 4 diagonal lines over the front
    and back of the shoulders.  Each line has an increase on either side.

    Tutorial for a well-documented raglan here:
    https://blog.tincanknits.com/2013/10/25/lets-knit-a-sweater/"""

    # Adjusting from collar to start of raglan
    instruction_string = ""
    # the final stitch count is bust_stitches + 2 * arm stitches
    # but that includes the added armpit stitches on both sides+sleeves
    working_stitches = bust_stitches + (2 * arm_stitches) - (4 * armpit_stitches)

    # Work backwards and see if you get the collar number
    calculated_neck = working_stitches - neck_to_bust_rows * increase_per_increase_row

    # if calculated_neck and neck_stitches don't match, make adjustments

    if calculated_neck > neck_stitches:
        # Add an increase row to go from your actual collar size to raglan start
        instruction_string += "Increase row: "
        instruction_string += increase_evenly(
            neck_stitches, calculated_neck - neck_stitches, in_the_round=True
        )

    if calculated_neck < neck_stitches:
        # you don't need to increase every row in the raglan section
        # We'll put the non-increase rows at the end before the armpit section
        no_increase_rows = 555  # FIXME

    # generate some standard raglan instructions
    # we're assuming the beginning of row is the middle of the back here
    body_start = bust_stitches / 2 - neck_to_bust_rows * 2 - armpit_stitches

    # in case our count is uneven
    front = math.ceil(body_start)
    back = math.floor(body_start)

    arm = arm_stitches - armpit_stitches - neck_to_bust_rows * 2

    instruction_string += f"Marker setup: k{math.floor(back/2)}, pm, k{arm} (arm), pm, "
    instruction_string += f"k{front}, pm, k{arm} (arm), pm k{math.ceil(back/2)}"

    return instruction_string

