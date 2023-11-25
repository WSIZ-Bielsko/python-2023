import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Drapieżnik morski poluje na ryby; z jego rewirze pojawiła się pewna grupa ryb; ich wielkości zadane są
listą `fishes`. Wiadomo, że drapieżnik może zjeść tylko ryby o wielkości >= min_size, i <= max_size. 
Funkcja powinna obliczyć na ile ryb z grupy drapieżnik może zapolować. 

"""


def eat_small_fish(fishes: list[int], min_size: int, max_size: int) -> int:
    # your code here
    pass

class TestEngine1(unittest.TestCase):

    def test_1(self):
        self.assertEqual(eat_small_fish([1, 2, 3, 4, 5], 2, 3), 2)

    def test_2(self):
        self.assertEqual(eat_small_fish([1, 1, 1, 2, 2], 2, 3), 2)

    def test_3(self):
        self.assertEqual(eat_small_fish([1, 10], 2, 3), 0)


if __name__ == '__main__':
    unittest.main()
