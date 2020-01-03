# -*- coding: utf-8 -*-

"""setuptools control."""

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('tagme/tagme.py').read(),
    re.M
    ).group(1)

setup(
    name="tagme",
    packages=["tagme"],
    entry_points={
        "console_scripts": ['bootstrap = tagme.tagme:main']
        },
    install_requires=[
        'Gooey',
        ],
    version=version,
    description="Python command line application to set tags in filename.",
    long_description="TBD",
    author="Arns & Kristina Udovič",
    author_email="zordsdavini@gmail.com, kristina.udoviciene@gmail.com",
    url="https://github.com/zordsdavini/TagMe",
    )
