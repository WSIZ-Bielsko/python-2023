from beautiful_necklace import is_necklace_beautiful


def test_short_ones():
    assert is_necklace_beautiful('*') is True
    assert is_necklace_beautiful('-') is False
    assert is_necklace_beautiful('*-') is True
    assert is_necklace_beautiful('-*') is True
    assert is_necklace_beautiful('**') is False
    assert is_necklace_beautiful('*-*') is False


def test_simple():
    assert is_necklace_beautiful('---*-*---') is True
    assert is_necklace_beautiful('---*-*') is True
    assert is_necklace_beautiful('---*-*-') is True
    assert is_necklace_beautiful('*-*----') is True
    assert is_necklace_beautiful('---**----') is False
    assert is_necklace_beautiful('---*--*----') is False


def test_simple_longer():
    assert is_necklace_beautiful('-*-*-*-*--') is True
    assert is_necklace_beautiful('------*-*-*---') is True
    assert is_necklace_beautiful('--*----*-*-*---') is False


def test_circular():
    assert is_necklace_beautiful('*-*---*') is False
    assert is_necklace_beautiful('-*-*---**') is False
    assert is_necklace_beautiful('-*---*') is True
    assert is_necklace_beautiful('*-*---*--') is False
    assert is_necklace_beautiful('*-*---*-*-') is True
