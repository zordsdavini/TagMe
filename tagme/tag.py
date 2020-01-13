import os
import re


class Tag():
    TAG_LIST = ['F', 'W', 'ZY', 'DO', 'KRI', 'NAG', 'DUM', 'ST', 'FE', 'AU']
    TAG_PATTERN = '_[A-Z_]+__'

    def mod_tag(self, tags: list) -> str:
        if len(tags) == 0:
            raise Exception('TAG_LIST should not be empty')

        modified: str = ''
        for i in tags:
            modified = modified + '_' + i

        modified = modified + '__'
        return modified

    def extract_tag(self, file_name: str) -> list:
        match_tag = re.search(self.TAG_PATTERN, file_name)
        if match_tag is None:
            return []
        etag_list = []
        for i in match_tag.group(0).split('_'):
            if i != '':
                etag_list.append(i)
        return etag_list

    def check_tags(self, tags: list) -> list:
        current_tag: list = []

        for i in self.TAG_LIST:
            if i in tags:
                current_tag.append(i)
        for i in tags:
            if i not in self.TAG_LIST:
                raise Exception('tag %s is not supported' % i)
        return current_tag

    def prepare_filename(self, path: str) -> str:
        file_name = os.path.basename(path)
        return re.sub(self.TAG_PATTERN, '', file_name)

    def add_tag(self, tags: list, path: str):
        file_name = os.path.basename(path)
        extracted_tags = self.extract_tag(file_name)
        tags = self.check_tags(tags + extracted_tags)
        dest = self.mod_tag(tags) + self.prepare_filename(path)
        source = path
        dest = os.path.dirname(path) + '/' + dest
        os.rename(source, dest)

path_test = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers/_W__peiza1.jpeg'
#a = Tag()
#a.mod_tag(['F', 'W'])
#a.add_tag(['F', 'W'], path_test)

#assert a.mod_tag(['F']) == '_F__', 'BAD'
