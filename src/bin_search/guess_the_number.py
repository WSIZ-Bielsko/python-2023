from random import randint


def game(a_min: int, a_max: int, n_attempts: int):
    secret_number = randint(a_min, a_max)
    b_min, b_max = a_min - 1, a_max + 1
    for attempt in range(1, n_attempts + 1):
        suggestion = b_min + (b_max - b_min) // 2
        guess = int(input(f'attempt ({attempt}/{n_attempts}), (suggestion: {suggestion}) your guess: '))
        if guess > secret_number:
            print('szukana liczba jest mniejsza')
            b_max = guess
        elif guess < secret_number:
            print('szukana liczba jest większa')
            b_min = guess
        else:
            print('trafione! brawo!')
            return
    print('wtopa; try again...')


if __name__ == '__main__':
    game(a_min=1, a_max=1000, n_attempts=10)
