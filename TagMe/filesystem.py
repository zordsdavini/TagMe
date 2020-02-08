import os
from TagMe.tag import Tag


class FileSystem:
    def __init__(self):
        pass
        self.tag = Tag()

    def get_files(self, dir_path: str) -> list:
        list_files: list = []
        for dirpath, dirnames, files in os.walk(dir_path):
            #print(f'Found directory: {dirpath}')
            for file_name in files:
                list_files.append(os.path.join(dirpath, file_name))
        #print(list_files)
        return list_files

    def get_file_names(self, dir_path: str) -> list:
        list_file_names: list = []
        for i in self.get_files(dir_path):
            #list_file_names.append(os.path.basename(i))
            list_file_names.append(self.tag.prepare_filename(i))
        #print(list_file_names)
        return list_file_names

    def file_exists(self, file_path: str, dir_dest: str) -> bool:
        file_name_source: str = self.tag.prepare_filename(file_path)
        list_file_names_dest: list = self.get_file_names(dir_dest)
        for i in list_file_names_dest:
            if file_name_source == i:
                return True
        return False

    def delete_file(self, file_path: str):
        try:
            os.remove(file_path)
            print(file_path)
        except OSError as err:
            print(f'Error: {file_path} : {err.strerror}')
            return

        dir_name = os.path.dirname(file_path)
        if len(self.get_files(dir_name)) == 0:
            try:
                os.rmdir(dir_name)
                print(dir_name)
            except OSError as err:
                print(f'Error: {dir_name} : {err.strerror}')


#test_path = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers1/00049.jpg'
#a = FileSystem()
#a.delete_file(test_path)
#a.get_files(test_path)
#b=a.get_file_names(test_path)
#print(b)