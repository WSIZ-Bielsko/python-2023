from makepi import get_pi_as_string


if __name__ == '__main__':
    d = dict()

    s = get_pi_as_string(1000)

    for i in range(10):
        d[str(i)] = 0

    for c in s[2:]:
        d[c] += 1

    for k in d:
        print(f'{k:3} -> {d[k]}')
