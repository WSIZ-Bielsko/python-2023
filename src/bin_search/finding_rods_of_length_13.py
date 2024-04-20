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


if __name__ == '__main__':
    seed(111)
    blues = [random() * 10 for _ in range(10000)]
    reds = [random() * 10 for _ in range(10000)]

    res = find_rods_of_length_13(blues, reds)  # 12.999999955730626
    print(res)
