# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.Sock: Functions for creating socks
"""


class Sock:
    def __init__(self):
        self.rows_per_inch = None
        self.stitches_per_inch = None
        self.circumference_at_top = None  # inches
        self.circumference_of_ankle = None  # inches
        self.length_from_sock_top_to_heel_bottom = None  # inches
        self.length_from_heel_to_toe = None # inches

        self.instructions = []
        self.cast_on_stitches = 0
        self.ankle_stitches = 0
        self.length_of_heel_flap = 0 # inches
        self.length_from_sock_top_to_heel_flap = 0 # inches
        self.number_of_decrease_rows = 0
        self.number_of_heel_flap_stitches = 0
        self.length_of_toe_decrease = 0 # inches
        self.length_from_heel_to_beginning_of_toe_decrease = 0 #inches


    def init(self,
             rows_per_inch=11,
             stitches_per_inch=9,
             circumference_at_top=10,
             circumference_of_ankle=9.5,
             length_from_sock_top_to_heel_bottom=7.75,
             length_from_heel_to_toe=10.5 ):

        self.rows_per_inch = rows_per_inch
        self.stitches_per_inch = stitches_per_inch
        self.circumference_at_top = circumference_at_top
        self.circumference_of_ankle = circumference_of_ankle
        self.length_from_sock_top_to_heel_bottom = length_from_sock_top_to_heel_bottom
        self.length_from_heel_to_toe = length_from_heel_to_toe

        self.get_cast_on_stitches()
        self.get_ankle_stitches()
        self.get_length_of_heel_flap()
        self.get_length_from_sock_top_to_heel_flap()
        self.get_number_of_heel_flap_stitches()
        self.get_length_of_toe_decrease()
        self.get_length_from_heel_to_beginning_of_toe_decrease()


    def round_down_even(self,n):
        answer = round(n)
        if not answer%2:
            return answer
        else:
            return answer - 1

    def round_up_even(self,n):
        answer = round(n)
        if not answer%2:
            return answer
        else:
            return answer + 1


    def get_cast_on_stitches(self):
        x = (self.stitches_per_inch * self.circumference_at_top) * .8
        self.cast_on_stitches = self.round_down_even(x)


    def get_ankle_stitches(self):
        x = (self.stitches_per_inch * self.circumference_of_ankle) * .8
        self.ankle_stitches = self.round_down_even(x)


    def get_length_of_heel_flap(self):
        x = self.ankle_stitches * 0.25
        y = self.rows_per_inch * .7
        self.length_of_heel_flap = round(x/y,2)


    def get_length_from_sock_top_to_heel_flap(self):
        x = self.length_from_sock_top_to_heel_bottom - self.length_of_heel_flap
        self.length_from_sock_top_to_heel_flap = round(x,2)


    def get_number_of_decrease_rows(self):
        x = (self.cast_on_stitches - self.ankle_stitches)/2
        self.number_of_decrease_rows = round_up_even(x)


    def get_number_of_heel_flap_stitches(self):
        x = (.5 * self.ankle_stitches) + 1
        self.number_of_heel_flap_stitches = x


    def get_length_of_toe_decrease(self):
        x = (0.25 * self.ankle_stitches) / self.rows_per_inch
        self.length_of_toe_decrease = round(x,2)


    def get_length_from_heel_to_beginning_of_toe_decrease(self):
        x = self.length_from_heel_to_toe_end - self.length_of_toe_decrease
        self.length_from_heel_to_beginning_of_toe_decrease = round(x,2)
