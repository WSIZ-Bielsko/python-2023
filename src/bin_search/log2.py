from math import log


def get_log_2(x: float) -> float:
    if x <= 0:
        return 0
    mi = -30
    mx = 30
    while True:
        y = (mx + mi) / 2
        if 2 ** y < x:
            mi = y
        else:
            mx = y
        if mi + 10 ** -5 >= mx:
            break
    # print(min, max)
    # print(2 ** min,2 ** max)
    return y
