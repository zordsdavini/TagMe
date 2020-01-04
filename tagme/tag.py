import os


class Tag():
    TAG_LIST = ['F', 'W', 'ZY', 'DO', 'KRI', 'NAG', 'DUM', 'ST', 'FE', 'AU']

    def mod_tag(self, tags: list) -> str:
        if len(tags) == 0:
            raise Exception('TAG_LIST should not be empty')

        modified: str = ''
        for i in tags:
            modified = modified + '_' + i

        modified = modified + '__'
        return modified

    def check_tags(self, tags: list) -> list:
        current_tag: list = []

        for i in self.TAG_LIST:
            if i in tags:
                current_tag.append(i)
        for i in tags:
            if i not in self.TAG_LIST:
                raise Exception('tag %s is not supported' % i)
        return current_tag

    def add_tag(self, tags: list, path: str):
        tags = self.check_tags(tags)
        dest = self.mod_tag(tags) + os.path.basename(path)
        source = path
        dest = os.path.dirname(path) + '/' + dest
        os.rename(source, dest)

#path_test = '/home/kri/Pictures/Favorites/Walpapers/Copy_Top Layers/peiza1.jpeg'
#a = Tag()
#a.mod_tag(['F', 'W'])
#a.add_tag(['F', 'W'], path_test)

#assert a.mod_tag(['F']) == '_F__', 'BAD'