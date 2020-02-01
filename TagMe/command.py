from TagMe.tag import Tag
from TagMe.filesystem import FileSystem


class Command:
    def process_add_tag_to_file(tags: list, files: list):
        tag_manager = Tag()
        for filename in files:
            tag_manager.add_tag(tags, filename)

    def process_add_tag_to_directory(tags: list, directory: str):
        tag_manager = Tag()
        filesystem = FileSystem()

        files = filesystem.get_files(directory)
        for filename in files:
            tag_manager.add_tag(tags, filename)
