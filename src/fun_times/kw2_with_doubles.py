from random import randint


def get_average_d6_2x_throws(throws: int) -> float:
    final_sum = 0
    for i in range(throws):
        throws_sum = 0
        while True:
            throw1 = randint(1, 6)
            throw2 = randint(1, 6)
            throws_sum += throw1 + throw2
            if throw1 != throw2:
                break

        final_sum += throws_sum

    average = final_sum / throws
    return round(average, 2)


if __name__ == '__main__':
    print(get_average_d6_2x_throws(1000000))
