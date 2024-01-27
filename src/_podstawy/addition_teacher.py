def check_result_of_addition(a: int, b: int, result: int):
    if a + b == result:
        print('wynik poprawny')
    else:
        print('blad dodawania')

    # print('wynik poprawny' if a + b == result else 'blad dodawania')


# check_result_of_addition(2, 4, 6)
# check_result_of_addition(2, 4, 5)
# check_result_of_addition(-2, 4, 2)

from random import randint

for i in range(5):
    a = randint(-5, 5)
    b = randint(-5, 5)
    res = int(input(f'podaj wynik {a}+{b}:'))
    check_result_of_addition(a, b, res)
