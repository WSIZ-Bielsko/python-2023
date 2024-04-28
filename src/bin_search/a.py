a = 3
w = [1, 3, 5, 6, 7, 8, 9, 10, 12]

x = [(a * 2 ** i in w) for i in range(10)]
print(x)
z = x.index(False)
print(z)
print(a * 2 ** z)
