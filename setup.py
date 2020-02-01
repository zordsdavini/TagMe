# -*- coding: utf-8 -*-

import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('TagMe/tagme.py').read(),
    re.M
    ).group(1)
short_descrription = re.search(
    '^__short_description__\s*=\s*"(.*)"',
    open('TagMe/tagme.py').read(),
    re.M
    ).group(1)

setup(
    name="tagme",
    packages=["TagMe"],
    entry_points={
        "console_scripts": ['tagme-cli = TagMe.tagme:main']
        },
    version=version,
    description=short_descrription,
    long_description="TBD",
    author="Arns & Kristina Udovič",
    author_email="zordsdavini@gmail.com, kristina.udoviciene@gmail.com",
    url="https://github.com/zordsdavini/TagMe",
    )
