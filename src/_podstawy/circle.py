from random import randint


def get_p_circle(n_randoms: int):
    cnt = 0
    M = 1000
    for _ in range(n_randoms):
        x = randint(-M, M)
        y = randint(-M, M)
        if x ** 2 + y ** 2 <= M ** 2:
            cnt += 1
    return cnt / n_randoms * 4


print(get_p_circle(10000000))
