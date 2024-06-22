from collections import deque
from random import choice


def load_board(file_name: str):
    board = []
    with open(file_name, 'r') as f:
        for ln in f.readlines():
            row = [int(x) for x in ln.split(' ')]
            board.append(row)
    return board


def show_board(board: list[list[int]]):
    print()
    for i, row in enumerate(board):
        print(f'row{i}', ' '.join([str(i) for i in row]))


def find_cheapest_left_to_right(board: list[list[int]]) -> tuple[int, int]:
    """
    Finds the lowest cost of crossing the board along a row, from left to right

    :param board:
    :return: tuple: (minimal_cost, row_number)
    """
    return (0, 0)


def find_cost_of_path(board: list[list[int]], path: list[tuple[int, int]]) -> int:
    """
    Finds the cost of the `path` on the `board` provided
    :param board:
    :param path:
    :return: cost of moving along the path
    """
    return 0


def get_possible_next_locations(current_locatoin: tuple[int, int], n_rows: int, n_cols: int) -> list[tuple[int, int]]:
    x, y = current_locatoin
    candidates = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    result = []
    for nx, ny in candidates:
        if nx < 0 or ny < 0 or nx >= n_rows or ny >= n_cols:
            continue
        result.append((nx, ny))
    return result


def walk_the_landscape(board: list[list[int]], n_steps, acceptable_terrain_cost: int):
    n_rows = len(board)
    n_cols = len(board[0])
    visited = set()
    visited.add((0, 0))

    maked_to_visit = deque()
    maked_to_visit.append((0, 0))

    for step in range(n_steps):
        if len(maked_to_visit) == 0:
            break
        at = maked_to_visit.popleft()
        print(f'visiting {at}')
        next_locations = get_possible_next_locations(at, n_rows, n_cols)
        for n_loc in next_locations:
            if n_loc in visited:
                continue

            if board[n_loc[0]][n_loc[1]] > acceptable_terrain_cost:
                continue

            print(f'marking {n_loc} for later visit')
            visited.add(n_loc)
            maked_to_visit.append(n_loc)

    for x, y in visited:
        board[x][y] = '.'


def walk_the_mylna_cave(board: list[list[int]], max_depth, acceptable_terrain_cost: int,
                        visited: set[tuple[int, int]], at: tuple[int, int]):
    if max_depth == 0:
        print(f'{at} --> too deep, exiting')
        return True
    n_rows = len(board)
    n_cols = len(board[0])
    print(f'visiting {at}')
    visited.add(at)
    next_locations = get_possible_next_locations(at, n_rows, n_cols)
    print(f'{next_locations=}')
    for n_loc in next_locations:
        print(f'   checking {n_loc}')
        if n_loc in visited:
            continue

        if board[n_loc[0]][n_loc[1]] > acceptable_terrain_cost:
            continue
        walk_the_mylna_cave(board, max_depth - 1, acceptable_terrain_cost,
                            visited=visited, at=n_loc)
    print(f'exiting {at}')


if __name__ == '__main__':
    import os

    print(f'starting in {os.getcwd()}')
    a: list[list[int]] = [[]]

    board1 = load_board('xx.txt')
    # print(board1)
    # show_board(board1)

    # walk_the_landscape(board1, 700, acceptable_terrain_cost=7)

    visited: set[tuple[int, int]] = set()
    walk_the_mylna_cave(board1, max_depth=250, acceptable_terrain_cost=7, visited=visited,
                        at=(0, 0))
    for at in visited:
        board1[at[0]][at[1]] = '.'

    show_board(board1)
    # find_cost_of_path(board1, [(0, 0), (0, 1), (0, 2), (1, 2)])  # 12
