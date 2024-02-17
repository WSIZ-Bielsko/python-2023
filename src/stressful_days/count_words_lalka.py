if __name__ == '__main__':
    with open('lalka-tom-pierwszy.txt', 'r') as f:
        lines = f.readlines()
    # lines: list[str], ... wszystkie linie z pliku "lalka-tom-pierwszy.txt"
    for ln in lines:
        ln = ln.lower()
        ln = ln.replace('-', ' ')
        words = ln.split(' ')
        # todo: find how ofted each word appears...; word has >=3 letters
        # hint... użyć dict ... "słowo" --> ile razy występuje (początkowo 0)

    # hint... zebrać słowa do listy typu w = [[5, 'aby'], [10, 'drzwi'], [4, 'drugi']]
    # potem dać w.sort()

