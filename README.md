# pyKnit
A set of tools for knitters to do math, create charts, and eventually more.

![pyknit](https://github.com/terriko/pyknit/workflows/pyknit/badge.svg?branch=main&event=push)
[![On PyPI](https://img.shields.io/pypi/v/pyknit)](https://pypi.org/project/pyknit/)

## Usage

pyKnit works best in conjunction with [Jupyter](https://jupyter.org/install).
This allows you to "mess around" with the functions and see the results in your
browser.  I like this especially for the ability to display the charts inline.

Make sure you install Jupyter and pyknit in the same place (e.g. in the same
virtualenv if you're using one) so that you can use `import pyknit` and have it
work. (You can [read more about how to install a python Package in Jupyter
here](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/).)

I prefer to use virtualenv and pip, so I set up my environment as follows:

```console
virtualenv -p python 3.8 venv-3.8-jupyter
source ~/venv-3.8-jupyter/bin/activate
pip install jupyterlab
pip install pyknit
jupyter-lab
```

From there, jupyter lab will open in a browser, and you can create a new notebook to play around.  When you're done, you can shut down the notebook server using `^C` in the console and typing `y` when it asks if you want to shut down.  You can deactivate the virtualenv by typing `deactivate` and pressing enter.

If you want to run it again later, you can do the following:

```console
source ~/venv-3.8-jupyter/bin/activate
jupyter-lab
```

(The virtualenv only needs to be created once, and you don't need to reinstall.)

If you don't want to use Jupyter, it will also work as any standard python library.

`pip install pyknit`

And then go ahead and import it into your Python program.  There's also a
minimal command line interface which could be expanded if anyone actually wants
to use it.

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
