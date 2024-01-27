from random import randint


def check_birthdays(n_birthdays: int) -> int:
    d = dict()
    for i in range(n_birthdays):
        d[randint(1, 365)] = 1
    return len(d)


if __name__ == '__main__':
    N = 1000
    with_duplicates = 0
    n_persons = 15
    for _ in range(N):
        real_size = check_birthdays(n_birthdays=n_persons)
        if real_size < n_persons:
            with_duplicates += 1

    print(f'all experiments: {N}')
    print(f'duplicates: {with_duplicates}')
