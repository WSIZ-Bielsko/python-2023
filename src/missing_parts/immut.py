def brrrrr(s: tuple) -> tuple:
    res = list(s)
    res[2] = 'x'
    return tuple(res)


if __name__ == '__main__':
    s = (1, 2, 3, 4)
    nowa = brrrrr(s)
    # has 's' been changed ???
    print(s)
    print(nowa)
