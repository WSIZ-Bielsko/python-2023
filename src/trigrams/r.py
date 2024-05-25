if __name__ == '__main__':
    s1 = {1, 2, 3, 4}
    s2 = {3, 4, 8, 9}
    # znaleźć takie elementy, które należą do s1 i do s2
    # ?

    result = set(s1)
    for s in s2:
        result.add(s)
    print(result)
    print(s1 | s2)
