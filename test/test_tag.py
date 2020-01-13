import pytest

from tagme.tag import Tag


TAG = Tag()


def test_mod_tag_empty():
    with pytest.raises(Exception, match='TAG_LIST should not be empty'):
        TAG.mod_tag([])


def test_mod_tag_simple():
    assert TAG.mod_tag(['F', 'W']) == '_F_W__'


def test_extract_tag_no_tag():
    assert TAG.extract_tag('koja15.py') == []


def test_extract_tag_simple():
    assert TAG.extract_tag('_F_ZY__koja15.py') == ['F', 'ZY']


def test_check_tag_not_supported():
    with pytest.raises(Exception, match='tag KOJA is not supported'):
        TAG.check_tags(['F', 'KOJA', 'W'])


def test_check_tag_fix_queue():
    assert TAG.check_tags(['ZY', 'F', 'DUM']) == ['F', 'ZY', 'DUM']


def test_prepare_filename_no_tags():
    assert TAG.prepare_filename('/a/b/c/koja15.py') == 'koja15.py'


def test_prepare_filename_remove_tags():
    assert TAG.prepare_filename('/a/_F_ZY__koja15.py') == 'koja15.py'
