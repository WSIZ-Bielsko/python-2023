import unittest

"""
Napisać funkcję (wpisać kod ↓↓), która podaje rozwiązanie następującego zadania:
Domyślamy się, że w pewnym napisie schowany został "shrug", czyli ¯\_(ツ)_/¯. 
Shrug może być ewentualnie podzielony na dwie części, czyli np. "¯\_(ツ....)_/¯" lub
"¯\_#######(ツ)_/¯" też zaliczamy do napisów zawierających shrug-a, ale już nie np
"¯\_###(ツ)###_/¯". Proszę napisać funkcję, która sprawdza czy w podanym napisie `line` zawarty jest shrug. 


"""


def has_hiddden_shrug(line: str) -> bool:
    # your code here
    pass


class TestEngine3(unittest.TestCase):

    def test_1(self):
        self.assertEqual(has_hiddden_shrug("¯\_(ツ)_/¯"), True)

    def test_2(self):
        self.assertEqual(has_hiddden_shrug("¯\_##(ツ)_/¯"), True)

    def test_3(self):
        self.assertEqual(has_hiddden_shrug("¯\_(ツ)##_/¯"), True)

    def test_4(self):
        self.assertEqual(has_hiddden_shrug("¯\_##(ツ)##_/¯"), False)

    def test_5(self):
        # Dodatkowe napisy przed shrugiem nie są dozwolone
        self.assertEqual(has_hiddden_shrug("##¯\_##(ツ)_/¯"), False)

    def test_6(self):
        # Shrugi z krótkimi rękoma nie są dozwolone
        self.assertEqual(has_hiddden_shrug("¯\(ツ)/¯"), False)


if __name__ == '__main__':
    unittest.main()
