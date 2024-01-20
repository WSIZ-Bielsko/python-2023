from dataclasses import dataclass

w = [1, 2, 3, 4, 5, 6, 7]

# wybrac liczby podzielne przez 3


print(7 % 3)  # reszta z dzielenia 7 przez 3

nowe_w = []
for x in w:
    if x % 3 == 0:
        nowe_w.append(x ** 2)

print(nowe_w)

w = [x ** 2 for x in w if x % 3 == 0]  # comprehension
print(w)


@dataclass
class User:
    id: int
    name: str


users = [User(1, 'Roman'), User(2, 'Xiao'), User(3, 'Bill')] # zwykla tablica
print(users)


ids = []
for u in users:
    ids.append(u.id)

print(ids)

iii = [u.id for u in users]
print(iii)




