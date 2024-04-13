def find_side_B(a: int, pp: int) -> int:
    """
    :param a: długość przyprostokątnej
    :param pp: pewna długość; mamy wybrać taką długość drugiej przyprostokątnej (b), by długość przeciwprostokątnej
                trójkąta (a,b,c) była conajmniej `pp`
    :return:
    """
    for b in range(0, 10 ** 9):
        c = (a ** 2 + b ** 2) ** 0.5  # tw. Pitagorasa
        if c >= pp:
            return b


def find_side_B_binary_search(a: int, pp: int) -> int:
    """
    :param a: długość przyprostokątnej
    :param pp: pewna długość; mamy wybrać taką długość drugiej przyprostokątnej (b), by długość przeciwprostokątnej
                trójkąta (a,b,c) była conajmniej `pp`
    :return:
    """
    b_min = 0
    b_max = 10 ** 9
    while b_max - b_min > 1:
        print(f'{b_min} {b_max}')
        b = (b_max + b_min) // 2
        c = (a ** 2 + b ** 2) ** 0.5  # tw. Pitagorasa
        if c >= pp:
            b_max = b
        else:
            b_min = b
    return b_max


if __name__ == '__main__':
    # print(find_side_B(a=5 * 10 ** 7, pp=8 * 10 ** 7))  # 62449980
    print(find_side_B_binary_search(a=5 * 10 ** 7, pp=8 * 10 ** 7))  # 62449980
