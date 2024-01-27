from datetime import datetime


def is_ok(d: int):
    cn = [0] * 10
    while d > 0:
        cn[d % 10] += 1
        d //= 10
    for i in range(10):
        if cn[i] != 0 and cn[i] != 2:
            return False
    return True


def is_even_beautiful(number: int) -> bool:
    snumber = str(number)
    for digit in '0123456789':
        c = snumber.count(digit)  # ile razy znak `digit` wystepuje w napisie `snumber`
        # c = count_chars_in_string(snumber, digit)
        if c != 0 and c != 2:
            return False
    return True


if __name__ == '__main__':
    st = datetime.now().timestamp()
    g = 0
    for i in range(10 ** 6):
        if is_even_beautiful(i):
            g += 1
    en = datetime.now().timestamp()
    print(f'done in {en - st:.3f}; good: {g}')
