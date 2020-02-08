import os
import re


class Tag:
    TAG_LIST = ['F', 'W', 'ZY', 'DO', 'KRI', 'NAG', 'DUM', 'ST', 'E', 'AU']
    TAG_PATTERN = '_[A-Z_]+__'

    def mod_tag(self, tags: list) -> str:
        ''' Create string from tags for file name'''
        if len(tags) == 0:
            raise Exception('TAG_LIST should not be empty')

        modified: str = ''
        for i in tags:
            modified = modified + '_' + i

        modified = modified + '__'
        return modified

    def extract_tag(self, file_name: str) -> list:
        '''Get list of tags from file name'''
        match_tag = re.search(self.TAG_PATTERN, file_name)
        if match_tag is None:
            return []
        etag_list = []
        for i in match_tag.group(0).split('_'):
            if i != '':
                etag_list.append(i)
        return etag_list

    def check_tags(self, tags: list) -> list:
        '''Check if tag exists in defined tag list; sorted as initial tag list'''
        current_tag: list = []

        for i in self.TAG_LIST:
            if i in tags:
                current_tag.append(i)
        for i in tags:
            if i not in self.TAG_LIST:
                raise Exception('tag %s is not supported' % i)
        return current_tag

    def prepare_filename(self, file_path: str) -> str:
        '''Remove all tags from defined file name'''
        file_name = os.path.basename(file_path)
        return re.sub(self.TAG_PATTERN, '', file_name)

    def remove_tag(self, tags:list, file_path:str):
        '''Remove defined tag from file name'''
        file_name = os.path.basename(file_path)
        extracted_tags = self.extract_tag(file_name)
        updated_tags = [i for i in extracted_tags if i not in tags]
        dest_file_name = self.mod_tag(updated_tags) + self.prepare_filename(file_path)
        dest_path = os.path.dirname(file_path) + '/' + dest_file_name
        os.rename(file_path, dest_path)
        print(dest_path)

    def add_tag(self, tags: list, file_path: str):
        '''Add defined tags to file name'''
        file_name = os.path.basename(file_path)
        extracted_tags = self.extract_tag(file_name)
        tags = self.check_tags(tags + extracted_tags)
        dest_file_name = self.mod_tag(tags) + self.prepare_filename(file_path)
        dest_path = os.path.dirname(file_path) + '/' + dest_file_name
        os.rename(file_path, dest_path)
        print(dest_path)

#path_test = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers/_W_ZY__peiza1.jpeg'
#tags = ['ZY','DO']
#a = Tag()
#a.remove_tag(tags, path_test)
#a.mod_tag(['F', 'W'])
#a.add_tag(['F', 'W'], path_test)

#assert a.mod_tag(['F']) == '_F__', 'BAD'
