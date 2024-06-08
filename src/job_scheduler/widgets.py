def get_minimum_screen_count(n_small_tiles: int, n_large_tiles: int):
    screens_needed_for_large = (n_large_tiles + 1) // 2
    free_space = screens_needed_for_large * 15 - n_large_tiles * 4

    space_needed_for_small_tiles = max(0, n_small_tiles - free_space)
    extra_screens_for_small = (space_needed_for_small_tiles + 14) // 15

    return screens_needed_for_large + extra_screens_for_small


if __name__ == '__main__':
    print(get_minimum_screen_count(n_small_tiles=5, n_large_tiles=2))  # 1
    print(get_minimum_screen_count(n_small_tiles=15, n_large_tiles=2))  # 2
    print(get_minimum_screen_count(n_small_tiles=1, n_large_tiles=1))  # 1
    print(get_minimum_screen_count(n_small_tiles=31, n_large_tiles=0))  # 3
