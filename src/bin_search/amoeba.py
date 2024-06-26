def get_final_amoeba_size(init_size: int, food: list[int]) -> int:
    amoeba_size = init_size
    food.sort()
    for el in food:
        if amoeba_size == el:
            amoeba_size *= 2

    return amoeba_size

# 1-liner solution (code golf; don't go for it!)
# def get_final_amoeba_size(init_size: int, food: list[int]) -> int:
#     return init_size * 2 ** ([(init_size * 2 ** i in food) for i in range(100)].index(False))


if __name__ == '__main__':
    w = [0, 1, 5, 12, ]

    w.sort()

    print(5 in w)  # True
    print(12 in w)  # True
    print(3 in w)  # False

    for e in w:
        print(e)
