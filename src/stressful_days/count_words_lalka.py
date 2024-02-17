if __name__ == '__main__':
    with open('lalka-tom-pierwszy.txt', 'r') as f:
        lines = f.readlines()
    for ln in lines:
        ln = ln.upper()
        ln = ln.replace('-', ' ')
        words = ln.split(' ')
        # todo: find how ofted each word appears...; word has >=3 letters

