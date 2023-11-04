def count_divisible_numbers(from_number: int, to_number: int, divisor: int):
    n_divisible = 0
    for x in range(from_number, to_number + 1):
        if x % divisor == 0:
            n_divisible += 1
    print(f'w przedziale [{from_number}..{to_number}] znajduje sie {n_divisible} liczb podzielnych przez {divisor}')


count_divisible_numbers(1, 10**6, 7)
