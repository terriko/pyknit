Pycon 2021 Presentation - pyKnit: Math Tools For Knitters
=========================================================

`Original slides with notes <https://docs.google.com/presentation/d/1Kr7Nmzgs5RCqx3kxyMDXwGNGe9Skq8E4bquLQhI3fdo/edit?usp=sharing>`_ (Link goes to Google Slides)


Slide 0
-------
Title slide reads as follows:

* pyKnit: Math Tools for Knitters.
* Presentation given by Terri Oda at PyCon 2021.

Slide 1
-------

Slide reads "Hi, I'm Terri" and features a picture of the speaker, a multiracial woman wearing a colourful knitted shawl around her neck like a scarf.

Hi, I’m Terri.  Normally, I talk about security, open source, mentoring, or artificial intelligence, but right now I’m on sabbatical so let’s talk about knitting.

Shawl: `Symphony by Tabetha Hendrick, yarn from Sweet Georgia Yarns <https://sweetgeorgiayarns.com/shop/symphony/>`_

Slide 2
-------

Slide features a two-coloured pink and peach lace shawl in progress on metal knitting needles, as well as a motif of blue "v" shapes at the bottom meant to represent knit stitches.

Probably if you chose to watch this talk you already know what knitting is, but just in case you want a refresher, it’s a process where you take a long length of yarn and turn it into a stretchy fabric by making a series of interlocking loops.  Knitting can be done by machines, and there’s a good chance you’re wearing some knit fabric right now: if you look at a t-shirt very closely you’ll see that it’s made teensy tiny little v’s of thread like the pattern I have on the bottom of my slides.  Many knit fabrics are made by machine, but today we’re going to talk about hand knitting, the stuff done with two pointy sticks and yarn.   

Shawl: `Romi Mystery 2021 <https://www.ravelry.com/patterns/library/romis-2021-spring-mystery-shawl-kal>`_
Yarn: `Romi Mystery 2021 kit from A Verb For Keeping Warm <https://www.averbforkeepingwarm.com/>`_

Slide 3
-------
Slide reads "Tools for Knitters" and contains some pictures described in more detail below.

When you think about tools for knitters, you probably think of yarn, knitting needles, maybe scissors (show all of these), a nice bag to carry things in.  If you’re actually a knitter you probably have a few more on hand, like stitch markers, a special ruler (show), an application for handling charts (show knitcompanion but make sure to use one of my charts).  If you're not a knitter, you probably didn't picture a calculator or a spreadsheet.

Upper left photo:
Yarn ball holder from Hansen Crafts https://hansencrafts.com/knitting-crochet-tools/yarn-ball-holder/ 
Yarn from The Fibre Co.
Sweater in progress: https://www.ravelry.com/projects/terriko/stepping-stones-cardigan  Stepping Stones Cardi by Rebecca McKenzie

Upper Right photo: Dollyville Care Package from KnittedWit and others: https://www.etsy.com/listing/1006196101/dollyville-care-package?ref=shop_home_active_1&crt=1

Bottom photo: Miscellaneous tools from Katrinkles Knitting Jewelery https://www.katrinkles.com/ 

Slide 4 
-------

Slide reads "pyKnit: math tools for knitters" and features a colourful striped sock in progress.

I got tired of using my calculator and spreadsheet to figure things out, and thought “why isn’t there a library for this?” and that’s how pyKnit was born.  It’s an open source project, written in python, that helps you do knitting math, which can be surprisingly involved and is actually more like solving algebraic equations than balancing a checkbook.  I love algebra enough that I got a whole degree in mathematics, but deriving equations over and over gets tedious.

Knitting: 2020 Advent Sock kit from MadeBySarahS https://www.madebysarahs.net/
Stitch Marker by Wee Ones Creations https://www.etsy.com/shop/weeones
Bag from Tom Bihn https://www.tombihn.com/products/ghost-whale-organizer-pouch

Slide 5
-------

Slide reads "Where is the math in knitting" and features a picture of a colourful brioche knit shawl in progress.

In order to understand why this is a great tool to add to your kit, you have to understand where and why we do math in knitting.  I’m not going to cover all the possible ways, but here’s a couple of very common places where it matters.

Knitting: Syncopation Shawl by PDXKnitterati https://pdxknitterati.com/patterns/patterns-shawls-and-wraps/syncopation/
Yarn: Gradient from Fierce Fibers in colour “Sinnerman” https://fiercefibers.com/ , sparkly charcoal from Anzula Fiber Arts https://anzula.com/ 
Bag from Tom Bihn https://www.tombihn.com/
Helmet from Nutcase

Slide 6
-------

Slide reads "Gauge: converting stitches or rows to measurements" and features a knit gague swatch and a ruler showing that it is 4 inches tall.  The gauge measurements listed next to it read "Gauge: 21 stitches and 31 rows = 10cm in Stockinette Stitch (Flat)"

Number 1, let’s talk about gauge.  When you see this in a knitting pattern, it looks like this: 21 stitches and 31 rows = 10 cm in Stockinette Stitch, knitted flat.  So before you knit the pattern, you cast on 21 stitches and knit 31 rows, then take your little square and wash it and dry it and measure it.  If you get exactly what the pattern says then you’re done and the math in the pattern will all work out for you.  If you didn’t quite get it, you can change needle size or yarn and try again until you do.  But if it doesn’t match, none of the measurements you get will be the same as what’s written.  For some projects, that doesn’t matter: if my scarf is 10% too long, I’m probably not going to notice.  But if my sweater is 10% too small, then there’s a good chance it’s not going to fit correctly.  So if you don’t get the correct gauge, you’ve got to be prepared to do a bunch of calculations yourself.

More gauge resources: https://blog.tincanknits.com/2013/08/17/gauge/

Yarn: The Fiber Co.
Ruler: Knitpicks 

Slide 7
-------
Slide contains the text "Shaping: Increasing & Decreasing Size" and contains a diagram from TinCanKnits showing a sweater in progress.

Next up is shaping.  If you’re knitting a sweater, you’re going to have a number of places where measurements change from one to another.  Probably the simplest to understand is a sleeve.  Your arm circumference at your shoulder or bicep is much larger than your arm measurement down at the wrist.  In the most common type of sleeve, you want to change smoothly from one measurement to the other to match the curve of your arm.  There’s lots of variants for fashion, but you can’t, say, put all the decreases at the top and expect that to fit most people.  Sometimes a pattern will just say “decrease evenly until you have X stitches” and it’s up to the knitter to figure out how to do that using (gasp) math, sometimes they’ll give explicit places to put those increases.  


Link to sweater diagram: https://blog.tincanknits.com/2013/10/25/lets-knit-a-sweater/

Slide 8
-------
Slide features some equations (described below) and the same sweater diagram as on the previous slide.

Given…
wrist_circumference 
bicep_circumference
arm_length
cuff_length
decreases_per_row

We want a pattern something like..
[decrease row, knit x rows in pattern] repeat y times

Such that...
wrist_circ = bicep_circ - (decreases_per_row * y) 
and
arm_length = (x+1) * y + cuff_length

Convert to stitches instead of measurements, solve for x and y but use only integers and spread out the remainder evenly too...


So if you’re customizing a sleeve, it starts out like this.  You know the length of your arm and how big you want the cuff to be, you’ll know the circumference you want at the bicep and wrist (which may be a bit bigger than your actual body measurements), so you figure out how much you want to decrease by subtracting the wrist measurement from the bicep one, then you figure out the length you want your decreases in, then you divide them… except remember, you can’t do this in measurements, you need to do it in stitches, which means you can only use integer numbers and have to deal with remainders somehow.  And then you might want to decrease more than one stitch per row (in fact 2 is the most common case) so …  It gets tedious to figure it all out every time.  And that’s for a simple sweater without much pattern, it gets much more complicated if you need to make sure the decreases fit into a lace pattern, for example.

Slide 9
-------
Silde reads "Shawl Shape Algorithms" and has pictures of some common shapes alongside equations.

A sleeve is basically a tube with different sized ends, but you can work all sorts of different shapes.  When you start looking for patterns you can see how knitting relates to geometry.  The first row has some pretty straightforward shapes: a rectangle where the size of each row remains constant.  A triangle where the length of each row increases each time, and a bias knit where the size of the row doesn’t change, but you put increases on one end and decreases on the other to move the pattern over with each row.  Then on the bottom you start to see shapes that occur in part because of the properties of the fabric you create and how it stretches -- a crescent shape which has extra increases on the edges, or a circular “pi shawl” shape with only a few increase rows with specific spacing.

Slide 10
--------
Slide title reads "Knitting Code" and shows a knitting chart alongside a written version of Row 16: "kfb, k to marker, \*l cable, r cable, k to marker, repeat from \* until you reach last marker, l cable, r cable, k3,  k2tog, k1"

In fact, if you look at a knitting chart, this symbols out of string thing is pretty explicit.  Here’s a knit chart I made as part of a shawl pattern, and down below is a written version.  Many knitting patterns come with both written and charted instructions because different people find one or the other easier.  In this chart on row 16, we’re reading from right to left, but you actually swap which direction you read the chart in based on the direction you’re going on the knitted piece. (show on finished piece.)  Down at the bottom you can see row 16 written out in a somewhat typical knitting shorthand.

The rest of the Patio Stones pattern: https://curiousity.ca/2020/patio-stones-pattern-preview/

Slide 11
--------

::

  def row16():
    knit_front_back()
    while not marker:
      knit()
    for repeat in repeat_sections:
      left_cable(1)
      right_cable(1)
      while not marker:
        knit() 
    left_cable(1)
    right_cable(1)
    for i in range(3):
      knit()
    knit_two_together()
    knit()

Row 16: kfb, k to marker, * l cable, r cable, k to marker, repeat from * until you reach last marker, l cable, r cable, k3,  k2tog, k1


For those of you who know more python than knitting, on the left there’s an interpretation of what that would look like.  Honestly, sometimes I miss whitespace in knitting patterns.  Because patterns were traditionally published in magazines, and people often still print them out or view them on phones or tablets, the syntax can be very terse.  Repeating a motif is common, and you can use stitch markers to note where the pattern changes or repeats happen.

Slide 12
--------

