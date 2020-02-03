# -*- coding: utf-8 -*-

"""Main run script."""

from argparse import ArgumentParser
from TagMe.tag import Tag
from TagMe.command import Command

__version__ = "0.0.7"
__short_description__ = "Command line application to set tags in filename."

actions = [
        'add_tag_to_file',
        'add_tag_to_directory',
        'remove_tag_from_file',
        'remove_tag_from_directory',
        'clean_directory',
        ]


def main():
    command_manager = Command()

    parser = ArgumentParser(prog="TagMe", description=__short_description__)

    parser.add_argument(
            'command',
            choices=actions,
            help='main command to be executed')
    parser.add_argument(
            '-f',
            '--files',
            nargs="*",
            help="file or files (separated by comma, ex. `a.jpg,b.jpg`) to process")
    parser.add_argument(
            '-t',
            '--tags',
            choices=Tag.TAG_LIST,
            nargs="*",
            help="tags (separated by comma) to process")
    parser.add_argument(
            '-d',
            '--directory',
            help="directory to process")

    args = parser.parse_args()

    if args.command == 'add_tag_to_file':
        print('Adding tag to file...')
        command_manager.process_add_tag_to_file(
                args.tags,
                args.files)

    elif args.command == 'add_tag_to_directory':
        print('Adding tag to directory...')
        command_manager.process_add_tag_to_directory(
                args.tags,
                args.directory)
