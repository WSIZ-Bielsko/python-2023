import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Liczbę nazywamy "parzyście-piękną" jeśli każda z jej cyfr występuje w niej dokładnie dwa razy. 
Np. liczby 2121, 2211, 321123 są parzyście piękne, choć np. 121, 2222, 33441156 już nie. 
Napisać funkcję która sprawdzi, czy podana liczba `number` jest parzyście piękna. 

"""


def count_chars_in_string(s: str, char: str):
    """
    Counts the number of occurrances of `char` in `s`.
    :param s:
    :param char:
    :return:
    """
    i = 0
    for c in s:
        if c == char:
            i += 1
    return i


def is_even_beautiful(number: int) -> bool:
    snumber = str(number)
    for digit in '0123456789':
        # c = snumber.count(digit)  # ile razy znak `digit` wystepuje w napisie `snumber`
        c = count_chars_in_string(snumber, digit)
        if c != 0 and c != 2:
            return False
    return True


class TestEngine6(unittest.TestCase):

    def test_1(self):
        self.assertEqual(is_even_beautiful(2233), True)

    def test_2(self):
        self.assertEqual(is_even_beautiful(11), True)

    def test_3(self):
        self.assertEqual(is_even_beautiful(1212), True)

    def test_4(self):
        self.assertEqual(is_even_beautiful(1221), True)

    def test_5(self):
        self.assertEqual(is_even_beautiful(121), False)

    def test_6(self):
        self.assertEqual(is_even_beautiful(33441156), False)

    def test_7(self):
        self.assertEqual(is_even_beautiful(2222), False)


if __name__ == '__main__':
    unittest.main()
