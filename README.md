# pyKnit

![pyKnit](https://raw.githubusercontent.com/terriko/pyknit/main/pyknit-logolong.png)

A set of tools for knitters to do math, create charts, and eventually more.

![pyknit](https://github.com/terriko/pyknit/workflows/pyknit/badge.svg?branch=main&event=push)
[![On PyPI](https://img.shields.io/pypi/v/pyknit)](https://pypi.org/project/pyknit/)

## Installing pyKnit

```
pip install pyknit
```

If you want to use the latest and greatest [grab pyknit from github](https://github.com/terriko/pyknit) and use `pip install -e` to install it in ["editable" mode](https://pip.pypa.io/en/stable/cli/pip_install/#install-editable).

```
git clone https://github.com/terriko/pyknit
pip install -e pyknit/
```

Note that when you're doing `pip install -e pyknit/` here that `pyknit/` refers to the directory.  (You don't really need the slash but it makes that more clear.) If you get an error about not being able to find `setup.py` you're probably giving it the wrong directory (and may need to `cd ..` to go up one directory).

## Jupyter-lab Usage

pyKnit works best in conjunction with [Jupyter](https://jupyter.org/install).
This allows you to "mess around" with the functions and see the results in your
browser.  I like this especially for the ability to display the charts inline.

Make sure you install Jupyter and pyknit in the same place (e.g. in the same
virtualenv if you're using one) so that you can use `import pyknit` and have it
work. (You can [read more about how to install a python Package in Jupyter
here](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/).)

I prefer to use virtualenv and pip, so I set up my environment as follows:

```console
virtualenv -p python3.8 venv-3.8-jupyter
source venv-3.8-jupyter/bin/activate
pip install jupyterlab
pip install pyknit
jupyter-lab
```
***Developers may prefer to [get pyknit from github](https://github.com/terriko/pyknit) and use `pip install -e $pyknit_directory` in lieu of `pip install pyknit`  Remember to restart the notebook kernel to get any changes you've made in the pyknit directory while you're editing the code!***


From there, jupyter lab will open in a browser, and you can create a new notebook to play around.  When you're done, you can shut down the notebook server using `^C` in the console and typing `y` when it asks if you want to shut down.  You can deactivate the virtualenv by typing `deactivate` and pressing enter.

If you want to run it again later, you can do the following:

```console
source venv-3.8-jupyter/bin/activate
jupyter-lab
```

(The virtualenv only needs to be created once, and you don't need to reinstall.)

## Using PyKnit

```python
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
```

Running that gives a new size of 49 inches. This sweater was designed for +/- 2 inches (it says so in the pattern), so that's too big unless I love a really baggy sweater.


```python
size2 = pyknit.convert_stitch_measure(38, pattern_g, my_g)
size1 = pyknit.convert_stitch_measure(34, pattern_g, my_g)
print(f"{size2=}")
print(f"{size1=}")
```

Those give me 44.25 inches and 40 inches respectively (rounded to the nearest quarter inch, anyhow)

If I was aiming for exactly 42 inches chest circumference, I'd have the option
of either knitting the 44 inch one and having 2 inches positive ease (i.e. the
sweater would be a little loose) or the 40 inch one with -2 inches positive
ease (i.e. the sweater would stretch to fit me), and I would choose whichever
one I think I'd like better assuming my swatch is sufficiently stretchy.

This [SweaterFit Example file](https://github.com/terriko/pyknit/blob/main/documentation/SweaterFit.py) is here if you want to sub in your own swatch numbers.


[Here's an example of how to calculate sweater sleeve decreases using pyknit](https://github.com/terriko/pyknit/blob/main/documentation/SleeveDecreases.md) to get you started.

For those using Jupyter, there are also several full interactive notebooks available:

* [Sweater Sleeve Decreases](https://github.com/terriko/pyknit/blob/main/documentation/SleeveDecreases.ipynb)
* [Triangle Hat interactive hat pattern](https://github.com/terriko/pyknit/blob/main/documentation/TriangleHat.ipynb)
* [Sweater Fit from gauge swatches](https://github.com/terriko/pyknit/blob/main/documentation/SweaterFit.ipynb)

## Why pyKnit?

There's lots of great tools for knitters out there, but they're not open
source, which means if I don't like the way they work, I'm often stuck with
weird workarounds.  I thought it would be fun to make some knitting tools that
were a bit more flexible.

I knit during conference talks, and every year at PyCon I meet a few folk who
stop by to ask what I'm knitting and or to show me what they're working on.  So
I know there's enough of an intersection between the knitting and Python
communities for this to be fun for more than just me.

And finally, knitting involves a lot of math.  Not every knitter loves math,
and even those who do can get tired of calculating and recalculating.  So why
not let the computer do that work?  I'd like to imagine a world where I could
publish a pattern with an interactive notebook and let people fit sweaters
specifically to their measurements, or figure out how to adjust a shawl if
you want to use all of a pretty gradient skein of yarn, or have the option to
add calculated stitch counts to every single row of your pattern so people can
check if they messed something up.

It's going to be a while before we get to the complicated stuff, but you have
to start somewhere!

## Contributing

Got an idea for a function you wish we had?  Think you found a bug?  [Let us know via the issues](https://github.com/terriko/pyknit/issues).

Know open source and want to just get into it?  [Make a pull request here](https://github.com/terriko/pyknit/pulls)

Never contributed to open source before? Not sure what open source is? [Here's a guide on How to contribute to open source](https://opensource.guide/how-to-contribute/) that includes information on why you might want to and how to do it.  I work with new contributors regularly in my day job, so don't be shy!  I'm happy to help you figure it out.

If you find a security issue and want to contact me privately, [send me an
email](https://github.com/terriko/).  It might feel silly to talk about
security issues in knitting software, but it *does* parse things and display
things, so it's possible!

## License

pyKnit is licensed under the [GPL-2.0 License](https://github.com/terriko/pyknit/blob/main/LICENSE)
