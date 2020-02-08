from TagMe.tag import Tag
from TagMe.filesystem import FileSystem


class Command:
    def process_add_tag_to_file(self, tags: list, files: list):
        tag_manager = Tag()
        for file_path in files:
            tag_manager.add_tag(tags, file_path)

    def process_add_tag_to_directory(self, tags: list, directory: str):
        tag_manager = Tag()
        filesystem = FileSystem()

        files = filesystem.get_files(directory)
        for file_path in files:
            tag_manager.add_tag(tags, file_path)

    def process_remove_tag_to_file(self, tags: list, files: list):
        tag_manager = Tag()
        for file_path in files:
            tag_manager.remove_tag(tags, file_path)

    def process_remove_tag_to_directory(self, tags: list, directory: str):
        tag_manager = Tag()
        filesystem = FileSystem()

        files = filesystem.get_files(directory)
        for file_path in files:
            tag_manager.remove_tag(tags, file_path)

    def process_clean_directory(self, source_directory: str, directory: str):
        filesystem = FileSystem()

        files = filesystem.get_files(source_directory)
        for file_path in files:
            if filesystem.file_exists(file_path, directory):
                filesystem.delete_file(file_path)
