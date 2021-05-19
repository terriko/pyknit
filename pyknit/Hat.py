# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

#!python
"""
pyKnit: a set of tools for knitters to do math, create charts, customise
patterns and more

pyKnit.Hat: Functions for creating a hat
"""


class Hat:
    def crown_decreases(self, repeats: int, stitches: int):
        if repeats <= 0 or stitches <= 0:
            return("Invalid starting parameters")
        if stitches % repeats > 0: 
            # TODO we could add extra decreases for remainder instead of erroring
            return("Error: stitch count does not divide evenly")

        instructions = []
        current_stitches = stitches
        count_per_repeat = stitches/repeats

        while current_stitches - repeats > 0:
            current_stitches = current_stitches - repeats
            if count_per_repeat - 2 > 0:
                instructions.append(f"[k{int(count_per_repeat-2)}, k2tog] repeat {repeats} times ({current_stitches} stitches)")
            else:
                instructions.append(f"k2tog {repeats} times ({current_stitches} stitches)")

            instructions.append(f"Knit 1 round") 
            count_per_repeat = count_per_repeat - 1
        instructions.append("Cut yarn leaving 4 inch tail, thread through remaining stitches and pull closed")
        return(instructions)
