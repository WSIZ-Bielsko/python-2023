from random import randint


def get_simple_average_of_d6(n_throws: int) -> float:
    """
    Return the average value in throws of a 1,2,...5,6 die (kostka).

    :param n_throws:
    :return:
    """
    # wygenerować `n_throws` liczb całkowitych z przedziału [1,6]; policzyć sumę i zwrócić suma/n_throws


def get_simple_average_of_2x_d6(n_throws: int) -> float:
    pass

if __name__ == '__main__':
    # throws = [randint(1, 6) for i in range(10)]
    # print(throws)
    print(get_simple_average_of_d6(n_throws=10000))