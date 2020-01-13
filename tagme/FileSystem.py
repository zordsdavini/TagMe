import os
#import tag


class FileSystem():

    def get_files(self, path_name: str) -> list:
        list_files: list = []
        for dirpath, dirnames, files in os.walk(path_name):
            #print(f'Found directory: {dirpath}')
            for file_name in files:
                list_files.append(os.path.join(dirpath, file_name))
        #print(list_files)
        return list_files

    def get_file_names(self, path_name: str) -> list:
        list_file_names: list = []
        for i in self.get_files(path_name):
            list_file_names.append(os.path.basename(i))
        #print(list_file_names)
        return list_file_names


#test_path = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers'
#a = FileSystem()
#a.get_files(test_path)
#a.get_file_names(test_path)
