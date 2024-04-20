from math import cos, sin


def get_distance(v0: float, angle: float):
    vx = v0 * cos(angle)
    vy = v0 * sin(angle)

    y = 0.00000000001
    x = 0
    dt = 0.001
    g = - 9.81
    while y > 0:
        y += vy * dt
        x += vx * dt
        vy = g * dt
        vx -= 0  # no air friction
    return x


if __name__ == '__main__':
    print(get_distance(10, 0.7))

    required_distance = 4
    # task: find the angle for which the get_distance(10,angle) is closest to `required_distance`
