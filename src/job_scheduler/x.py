if __name__ == '__main__':
    wagon_size = 13
    n_elems = 118
    wagons_needed = (n_elems + wagon_size - 1) // wagon_size
    print(wagons_needed)
    print(wagons_needed * wagon_size)
    print((wagons_needed-1) * wagon_size)
