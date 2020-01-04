# -*- coding: utf-8 -*-

"""Main run script."""

from gooey import Gooey, GooeyParser
from tagme.tag import Tag

__version__ = "0.0.3"


@Gooey(program_name="TagMe",
       program_description=__version__,
       advanced=True
       )
def main():
    parser = GooeyParser()

    parser.add_argument('filename', help="name of the file to process", widget="FileChooser")
    parser.add_argument('tags', help="select wanted tags", widget='Listbox', choices=Tag.TAG_LIST, nargs="*")

    args = parser.parse_args()
    print(args.filename, args.tags)

    tag_manager = Tag()
    tag_manager.add_tag(args.tags, args.filename)

    print("Executing TagMe version %s." % __version__)
    print("It works!")
