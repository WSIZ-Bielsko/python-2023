import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Mamy trzy liczby całkowite, podane w liście "data". Próbujemy stworzyć z tych liczb _kombinację_ 
o największej sumie, przy czym _kombinacją_ jest tablica podobna do "data", z tym, że pojedyncze jej
elementy mogą mieć zmieniony znak. 

Przykaład:
data = [1,-2,3]
kombinacje:
[1,-2,3]
[1,-2,-3]
[1,2,3]
[1,2,-3]
[-1,2,3]
[-1,2,-3]
[-1,-2,3]
[-1,-2,-3]

"""


def find_best_combination(data: list[int]) -> int:
    # your code here
    pass


class TestEngine2(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_best_combination([1, 1, -1]), 3)

    def test_2(self):
        self.assertEqual(find_best_combination([1, -5, -1]), 7)

    def test_3(self):
        self.assertEqual(find_best_combination([-2, 0, -1]), 3)


if __name__ == '__main__':
    unittest.main()
