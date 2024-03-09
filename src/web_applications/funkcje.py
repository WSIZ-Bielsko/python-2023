def add(a, b):
    return a + b


def mul(a, b):
    return a * b


def calculator(a, b, operation):
    return operation(a, b)


if __name__ == '__main__':
    print(add(2, 5))
    print(mul(2, 7))

    print(calculator(2, 7, mul))
    print(calculator(2, 7, add))
