from random import randint

if __name__ == '__main__':
    # w = []
    # w.append(1)
    # w.append(2)
    # w.append('kadabra')
    # print(w)
    # print(w[1])
    #
    # w[2] = 10
    # print(w)

    d = dict()  # "słownik"
    d[0] = 1  # key = 0, value = 1
    d[1] = 2  # key = 1, value = 2
    d[2] = 'kadabra'  # key = 2, value = 'kadabra
    d[12345678901] = 'xx1'

    d['cd12'] = 881  # key = 'cd12', value = 881

    for i in range(100):
        z = randint(0, 10 ** 10)
        key = f'u{z}'
        value = z + 1
        d[key] = value

    for k in d.keys():
        print(f'{k=} --> value={d[k]}')

    print(12345678901 in d)
    print(12345678902 in d)