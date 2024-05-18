d = dict()
d['a'] = 17
d['z'] = 1

print(d)
d['a'] += 1
print(d['a'])

from string import ascii_lowercase

print(ascii_lowercase)

s = 'kadabra'
for c in s:
    print('->', c)

xx = ['a'] * 17
print(xx)
zz = 'a' * 17
print(zz)
# zz[4] = 'x' # DOES NOT WORK


dane = ['abra', 'kadabra', 'hokus', 'pokus']
# result = ''
# for dn in dane:
#     result = result + dn  # THIS IS PROHIBITIVELY SLOW!!! DON'T USE!!!

result = ''.join(dane)

print(result)

