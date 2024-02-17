if __name__ == '__main__':
    lat = 49.821
    long = 19.049

    v_lat = -0.01
    v_lon = 0.02

    time = 0.0

    while lat < 50 and long < 20:
        lat += v_lat
        long += v_lon
        time += 0.01

    print(f'plane escaped from box after {time=}')


