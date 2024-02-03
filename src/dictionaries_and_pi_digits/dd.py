from collections import defaultdict

z = defaultdict(lambda: 0)

z['a'] += 1
print(z)