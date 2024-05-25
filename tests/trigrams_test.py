import pytest

from src.trigrams.solutions import get_trigrams, simple_trigram_similarity


def test_can_compute_trigrams():
    assert get_trigrams('ab') == ['  a', ' ab', 'ab ']
    assert get_trigrams('aaa') == ['  a', ' aa', 'aaa', 'aa ']
    assert get_trigrams('abc') == ['  a', ' ab', 'abc', 'bc ']
    assert get_trigrams('abcde') == ['  a', ' ab', 'abc', 'bcd', 'cde', 'de ']
    assert get_trigrams('hello') == ['  h', ' he', 'hel', 'ell', 'llo', 'lo ']


def test_can_compute_trigrams_padding():
    assert get_trigrams(' abc') == ['  a', ' ab', 'abc', 'bc ']
    assert get_trigrams('  abc') == ['  a', ' ab', 'abc', 'bc ']
    assert get_trigrams('abc    ') == ['  a', ' ab', 'abc', 'bc ']


def test_similarity():
    print(get_trigrams('abc'))  # ['  a', ' ab', 'abc', 'bc ']
    print(get_trigrams('abcd'))  # ['  a', ' ab', 'abc', 'bcd', 'cd ']

    in_both = ['  a', ' ab', 'abc']
    in_any = ['  a', ' ab', 'abc', 'bc ', 'bcd', 'cd ']

    assert simple_trigram_similarity('abc', 'abcd') == pytest.approx(0.5, abs=1e-3)
    assert simple_trigram_similarity('word', 'words') == pytest.approx(0.5714286, abs=1e-3)
    assert simple_trigram_similarity('abra', 'kadabra') == pytest.approx(0.3, abs=1e-3)
    assert simple_trigram_similarity('hokus', 'pokus') == pytest.approx(0.333, abs=1e-3)