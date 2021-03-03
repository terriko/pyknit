# Calculating Sweater Sleeve Decreases

Suppose I have a sweater pattern that I wish to modify so the arms fit me exactly.

First, I want to enter the data from my gauge swatch so I can do the right
calculations.  I like to take pictures of my washed and blocked swatches so I
have that data handy on my phone if I need it.

FIXME: Add photos here

The original sweater pattern was 24 stitches and 18 rows for a 4x4inch swatch, but my row count didn't line up, so I know I'm going to be doing something different than the original pattern.  Let's import what I've got into a swatch.  You can either install pyknit or get a copy from github and run python from that directory so you can import it.  Either way.  These examples show what it looks like from the python command line (that's what the >>> are about) so leave off the >>> if you're cutting and pasting.

``python
>>> import pyknit
>>> sweaterSwatch = Swatch(row_count=18, row_measure=3.25, stitch_count=24, stitch_measure=4, units="in")
```

Then I can go measure the sleeve against my arm.  In this case, I already had the top of the sleeve because this was a raglan sweater and the directions called for 2 inches of straight knitting first.  I decide I want another 11 inches of sleeve.

```python
>>> print(sweaterSwatch.measurement_to_rows(11))
61
```

Okay, so that's another 61 rows.  

Looking back at the pattern, I hve a starting count of 59 stitches and want an ending count of 43.  (I check the measurement from the pattern diagram to see if I really want the sleeve that size, but it turns out that the sleeve width is fine so I'm not customizing it.)  This pattern uses a fairly common 2-stiches decreased in every decrease row pattern.  So let's enter that all into pyknit:

```python
>>> print(pyknit.sleeve_decreases(61, starting_count=59, ending_count=43, decrease_per_row=2))
[decrease row, do 7 rows in pattern] * 5 times, [decrease row, do 6 rows in pattern] * 3 times
```

And there we have it!  

Let's double-check against my original pattern, though, just in case.  The original pattern had decreases every 9 rounds 8 times total.  We're still 8 times total, but because I wanted a shorter sleeve than the original pattern, I'm doing my decreases more frequently.  That all makes sense, so now it's time to knit!

