# Copyright (C) 2021 Terri Oda
# SPDX-License-Identifier: GPL-2.0-or-later

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().split("\n")

setuptools.setup(
    name="pyknit",
    version="0.0.4",
    author="Terri Oda",
    author_email="terri@toybox.ca",
    description="A set of tools for knitters to create charts and eventually more.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/terriko/pyknit",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["pyknit = pyknit.pyknit:main"],
    },
    install_requires=requirements
)
