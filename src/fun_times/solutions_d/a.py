import random


def game() -> int:
    position = 0
    rolls = 0
    while position < 10:
        roll = random.randint(1, 6)
        position += roll
        rolls += 1
        if position > 10:
            break
    return rolls



if __name__ == '__main__':

    num_simulations = 10000
    total_rolls = 0

    for i in range(num_simulations):
        total_rolls += game()

    average_rolls = total_rolls / num_simulations
    print("Średnia liczba rzutów to:", average_rolls)
