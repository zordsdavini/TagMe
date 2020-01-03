# -*- coding: utf-8 -*-

"""Main run script."""

from gooey import Gooey, GooeyParser

__version__ = "0.0.3"


@Gooey(name="TagMe")
def main():
    parser = GooeyParser(description=__version__)
    parser.add_argument('Filename', widget="FileChooser")

    args = parser.parse_args()

    print("Executing TagMe version %s." % __version__)
    print("It works!")
