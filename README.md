# TagMe
Tag multiple files by rename. Tag should appairs in filename. This is command line app. To get UI you can use
[https://github.com/zordsdavini/TagMe-gooey].

Supported commands:
  - add_tag_to_file - select one or many files sepparated by comma and add tags that can be sepparated by comma
  - add_tag_to_directory - add tags to given directory
  - remove_tag_from_file - TBD
  - remove_tag_from_directory - TBF
  - clean_directory - TBD


## Testing command
To run directly from source code:
- `$ ./tagme-runner.py arg1 arg2`

## Installation
`# python setup.py install`

## Run
To run command: `tagme-cli`

ex., `tagme-cli add_tag_to_file -t F W -f /home/a/o/e/www.j /home/a/o/e/www2.j`
