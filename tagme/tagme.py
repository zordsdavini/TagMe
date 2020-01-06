# -*- coding: utf-8 -*-

"""Main run script."""

from gooey import Gooey, GooeyParser
from tagme.tag import Tag

__version__ = "0.0.3"
actions = [
        'add_tag_to_file',
        'add_tag_to_directory',
        'remove_tag_from_file',
        'remove_tag_from_directory',
        'clean_directory',
        ]


@Gooey(program_name="TagMe",
       program_description=__version__,
       advanced=True
       )
def main():
    parser = GooeyParser()
    parser.add_argument('actions',
                        help="select wanted action",
                        widget='Listbox',
                        choices=actions,
                        nargs="*"
                        )

    subs = parser.add_subparsers(help='commands', dest='commands')

    add_tag_to_file_parser = subs.add_parser(
            'add_tag_to_file', help='add tags to selected files'
            )
    add_tag_to_file_parser.add_argument('filename', help="name of the file to process", widget="FileChooser")
    add_tag_to_file_parser.add_argument('tags', help="select wanted tags", widget='Listbox', choices=Tag.TAG_LIST, nargs="*")

    args = parser.parse_args()

    if args.actions == 'add_tag_to_file':
        print('Adding tag to file...')
        add_tag_to_file(args.tags, args.filename)


def add_tag_to_file(tags: list, filename: str):
    tag_manager = Tag()
    tag_manager.add_tag()
