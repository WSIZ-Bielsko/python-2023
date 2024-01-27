w = [2, 4, 9, 11]  # list[int]
#    0  1  2  3

print(w)
w.append(99)
print(w)

print(w[0])  # odczytywanie
print(w[3])

w[0] = 1  # zapis
print(w)

print(99 in w)  # True
print(len(w))  # 5, liczba elementów w liście

# [1, 4, 9, 11, 99]

print(w[:3])  # elementy listy `w` do elementu o indeksie 3 wyłącznie
print(w[3:])  # elementy listy od indeksu 3 (włącznie) do końca

zz = w[2:4]  # elementy listy między indeksami: 2 (włącznie) i 4 (wyłącznie)

print(w[-1])  # ostatni element
print(w[-2])

w.sort()  # po tej operacji lista jest posortowana rosnąco, [1, 4, 9, 11, 99]
print(w)
w.sort(reverse=True)  # sortowanie malejące
print(w)
