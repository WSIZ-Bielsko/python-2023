from datetime import datetime
from random import random, seed


def find_rods_of_length_13(blues: list[float], reds: list[float]) -> float:
    """
    Trzeba wybrać jeden element z blues i jeden z reds tak by suma długości tych elementów była jak najbliższa 13.
    :param blues:
    :param reds:
    :return:
    """
    best_length = 0
    best_dist = 10000
    for b in blues:
        for r in reds:
            if abs(13 - b - r) < best_dist:
                best_length = b + r
                best_dist = abs(13 - b - r)
    return best_length


def find_rods_of_length_13_bsearch(blues: list[float], reds: list[float]) -> float:
    """
    Trzeba wybrać jeden element z blues i jeden z reds tak by suma długości tych elementów była jak najbliższa 13.
    :param blues:
    :param reds:
    :return:
    """
    best_length = 0
    best_dist = 10000
    reds.sort()

    GOAL = 13

    for b in blues:

        left = 0
        rght = len(reds) - 1

        for _ in range(200):
            mid = (left + rght) // 2
            if b + reds[mid] > GOAL:
                rght = mid
            else:
                left = mid
            if rght == left + 1: break

        # ↓↓↓↓
        if left == 0: left = 1
        if rght == len(reds) - 1: rght = len(reds) - 2

        candidates = reds[left - 1:rght + 2]

        for r in candidates:
            if abs(GOAL - b - r) < best_dist:
                best_length = b + r
                best_dist = abs(13 - b - r)

    return best_length


def ts() -> float:
    return datetime.now().timestamp()


if __name__ == '__main__':
    seed(111)
    blues = [random() * 10 for _ in range(1000000)]
    reds = [random() * 10 for _ in range(1000000)]
    print(blues[:3])

    st = ts()

    # res = find_rods_of_length_13(blues, reds)         # 12.999999955730626
    res = find_rods_of_length_13_bsearch(blues, reds)  # 12.999999955730626

    en = ts()
    print(res)
    print(f'execution time: {en - st:.4f}s')
