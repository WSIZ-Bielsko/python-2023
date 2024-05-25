from string import ascii_lowercase

s = ascii_lowercase

d = dict()
for i in s:
    d[i] = 0

print(d)
request = 'kadabra'
for c in request:
    d[c] += 1

print(d)

delivered = 'karramba'
for c in delivered:
    d[c] -= 1

print(d)

missing, surplus = [], []
for c in ascii_lowercase:
    if d[c] > 0:
        missing.append(c * d[c])
    elif d[c] < 0:
        surplus.append(c * (-d[c]))

print(''.join(missing), ''.join(surplus))
