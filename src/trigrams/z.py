


if __name__ == '__main__':
    f = [' ff', 'xyz', 'aaa', 'bbc', 'aaa', ' ff']
    # zadanie -- znaleźć _unikalne_ napisy z listy f (tu: jest ich 4)
    s = set(f)
    print(s)
    print(type(s)) #<class 'set'>
    x = list(s)
    print(x)