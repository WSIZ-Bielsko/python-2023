# s = 'abc123'
# for c in s:
#     print(c, c.isdigit())
#
# f = '1234' # napis
# number_f = int(f) # zamienia napis 'f' na liczbę
#
# d = 5
# str_d = str(d) # napis '5' odpowiadający wartości zmiennej `d`


f = ['1', '5', '9']  # list[str]
f.sort(reverse=True)
print(f)
print(''.join(f))


line = 'abc123abc'
# hokus pokus
w = []
for c in line:
    if c.isdigit():
        w.append(c)
w.sort(reverse=True)
print(w)


f = ['1', '2', '3']