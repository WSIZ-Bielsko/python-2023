from random import randint


d = dict()
for i in range(10):
    d[str(i)] = 0


for _ in range(23000):
    liczba = randint(0,9)
    d[str(liczba)] += 1

for k in d:
    print(f'{k:3} -> {d[k]}')


