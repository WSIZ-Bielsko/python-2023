def load_board(file_name: str):
    board = []
    with open(file_name, 'r') as f:
        for ln in f.readlines():
            row = [int(x) for x in ln.split(' ')]
            board.append(row)
    return board


def show_board(board: list[list[int]]):
    for row in board:
        print(' '.join([str(i) for i in row]))


def find_cheapest_left_to_right(board: list[list[int]]) -> tuple[int, int]:
    """
    Finds the lowest cost of crossing the board along a row, from left to right

    :param board:
    :return: tuple: (minimal_cost, row_number)
    """
    return (0,0)


if __name__ == '__main__':
    a: list[list[int]] = [[]]

    board1 = load_board('landscape_1.txt')
    # print(board1)
    show_board(board1)
