import random


def game() -> int:
    position = 0
    n_rolls = 0
    while position < 10:
        roll = random.randint(1, 6)
        position += roll
        n_rolls += 1

    return n_rolls


# todo: można sprawdzić jak uruchomić to zadanie na wszystkich core'ach procesora (i przyspieszyć wynik o np. x24)
# sprawdzić chatgpt: "how to use process pool executor"
if __name__ == '__main__':

    num_simulations = 1000000
    total_rolls = 0

    for i in range(num_simulations):
        total_rolls += game()

    average_rolls = total_rolls / num_simulations
    print("Średnia liczba rzutów to:", average_rolls)
