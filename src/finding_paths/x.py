if __name__ == '__main__':
    visited = set()

    p = [(0, 0), (1, 1), (3, 7)]
    for x in p:
        visited.add(x)


    print((1,1) in visited)
