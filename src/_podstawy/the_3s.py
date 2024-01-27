w = 86231
print(type(w))
s = str(w)
print(s)
print(type(s))
print('1' in s)


#  --------------------

def count_lucky_numbers(from_number: int, to_number: int, lucky_char: str):
    n_numbers = 0
    for x in range(from_number, to_number + 1):
        s = str(x)
        if lucky_char in s:
            n_numbers += 1

    print(f'liczb z "{lucky_char}" w przedziale [{from_number}..{to_number}] jest: {n_numbers}')


count_lucky_numbers(1, 300, '3')
count_lucky_numbers(300, 1247, '7')
# count_lucky_numbers(1, 10 ** 8, '7')
