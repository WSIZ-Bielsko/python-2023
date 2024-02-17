from random import randint
import matplotlib.pyplot as plt

def get_chance_to_reach_position(position: int, n_rolls: int) -> float:
    wins = 0
    for _ in range(n_rolls):
        current_position = 0
        n_throws = 0
        while current_position != position and n_throws < n_rolls:
            throw = randint(1, 6)
            n_throws += 1

            if throw < 6:
                current_position += throw
            else:
                current_position = 0

            if current_position == position:
                wins += 1
                break
    chance = wins / n_rolls
    return chance


def get_smoothed_chance(n_repetitions, position, n_rolls):
    s = 0
    for i in range(n_repetitions):
        s += get_chance_to_reach_position(position, n_rolls)
    return s / n_repetitions


if __name__ == '__main__':
    # print(f'szansa na wygranie to {get_smoothed_chance(n_repetitions=30, position=30, n_rolls=10) * 100:.2f}%')
    ppos = []
    chance = []
    for pos in range(40):
        ppos.append(pos)
        chance.append(get_smoothed_chance(1000, pos, 10))

    plt.plot(ppos, chance)
    plt.show()
