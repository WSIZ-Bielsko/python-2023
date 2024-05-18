from src.missing_parts.solution_missing_parts import find_missing_and_surplus_parts


def test_simple():
    missing, surplus = find_missing_and_surplus_parts('ab', 'b')
    assert missing == 'a'
    assert surplus == ''


def test_simple2():
    missing, surplus = find_missing_and_surplus_parts('ab', 'aab')
    assert missing == ''
    assert surplus == 'a'


def test_bulk():
    assert find_missing_and_surplus_parts('ab', 'abc') == ('', 'c')
    assert find_missing_and_surplus_parts('aaaabbbb', 'aaaabbbc') == ('b', 'c')
    assert find_missing_and_surplus_parts('abbc', 'abc') == ('b', '')

def test_extra():
    assert find_missing_and_surplus_parts('aaaaa', 'aa') == ('aa', '')
