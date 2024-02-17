from random import randint


def get_average_d6_2x_throws(throws: int) -> float:
    final_sum = 0
    for i in range(throws):
        throw1 = randint(1, 6)
        throw2 = randint(1, 6)
        summed_throws = throw1 + throw2
        final_sum += summed_throws
    average = final_sum / throws
    return round(average, 2)


if __name__ == '__main__':
    print(get_average_d6_2x_throws(100000))
