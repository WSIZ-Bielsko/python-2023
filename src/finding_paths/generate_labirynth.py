from random import randint


def generate_map(file_name: str, n_rows: int, n_cols: int,
                 min_terrain_level: int, max_terrain_level: int):
    lines = []
    for _ in range(n_rows):
        ln = [str(randint(min_terrain_level, max_terrain_level)) for c in range(n_cols)]
        lines.append(' '.join(ln) + '\n')
    lines[-1] = lines[-1][:-1]

    with open(file_name, 'w') as f:
        f.writelines(lines)


if __name__ == '__main__':
    generate_map('xx.txt', 40, 40, 1, 8)
