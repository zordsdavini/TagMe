import os


class FileSystem():

    def get_files(self, path_name: str) -> list:
        listfiles = []
        for dirpath, dirnames, files in os.walk(path_name):
            #print(f'Found directory: {dirpath}')
            for file_name in files:
                listfiles.append(os.path.join(dirpath, file_name))
        print(listfiles)
        return listfiles


test_path = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers'
a = FileSystem()
a.get_files(test_path)






'''
        with os.scandir(path_name) as entries:
            for entry in entries:
                print(entry.name)
            return entry.name
'''