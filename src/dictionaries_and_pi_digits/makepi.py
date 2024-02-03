def make_pi(digits: int):
    q, r, t, k, m, x = 1, 0, 1, 1, 3, 3
    for j in range(digits):
        if 4 * q + r - t < m * t:
            yield m
            q, r, t, k, m, x = 10 * q, 10 * (r - m * t), t, k, (10 * (3 * q + r)) // t - 10 * m, x
        else:
            q, r, t, k, m, x = q * k, (2 * q + r) * x, t * x, k + 1, (q * (7 * k + 2) + r * x) // (t * x), x + 2


def get_pi_as_string(digits: int) -> str:
    my_array = []
    for i in make_pi(digits):
        my_array.append(str(i))
    return '3.' + ''.join(my_array[1:])

#
#
# my_array = my_array[:1] + ['.'] + my_array[1:]
# big_string = "".join(my_array)
# print("here is a big string:\n %s" % big_string)
# print(f'pi={get_pi_as_string(2000)}')
