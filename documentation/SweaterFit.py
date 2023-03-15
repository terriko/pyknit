import pyknit

# Sweater fit check math.  My gauge doesn't match the pattern but I like the
# fabric I got in my swatch and don't want to change the needle I'm using.
# What size should I knit?

pattern_g = pyknit.GaugeSwatch(
    stitch_count=27.5, stitch_measure=10, row_count=40, row_measure=4, units="in"
)
my_g = pyknit.GaugeSwatch(
    stitch_count=23.5, stitch_measure=10, row_count=33, row_measure=4, units="in"
)

# The closest size to my measurements is the 42in chest one, let's convert that

size3 = pyknit.convert_stitch_measure(42, pattern_g, my_g)
print(f"{size3=}")

size2 = pyknit.convert_stitch_measure(38, pattern_g, my_g)
size1 = pyknit.convert_stitch_measure(34, pattern_g, my_g)
print(f"{size2=}")
print(f"{size1=}")
