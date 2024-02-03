import math

if __name__ == '__main__':
    d = dict()  # key -> value
    d[1] = 12
    d[1] += 1
    d['Roman'] = 'Wolny'
    d['0'] = 88

    print(d)
    print('Roman' in d)  # sprawdza czy klucz jest w dict-cie

    d['Roman'] = 'Konieczny'
    print(d)

    p = math.pi
    print(p)

    for k in d:
        print(k, d[k])

    print('-----')
    print({i: i for i in range(1, 11)})
