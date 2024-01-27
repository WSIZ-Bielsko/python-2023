def get_distance(acceleration: float = 9.81, time: float = 1) -> float:
    return acceleration * time ** 2 / 2


# print(get_distance(time=2))  # 20


def get_acceleration(distance: float, time: float) -> float:
    for i in range(1000000):
        acc = 0.0001 * i
        if abs(get_distance(acc, time) - distance) < 0.01:
            print(f'{i=}')
            return acc
    return -1


print(get_acceleration(22, 2))
