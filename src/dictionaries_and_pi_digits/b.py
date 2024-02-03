ln = ['123\n', '456\n', '789\n']

# zadanie: zlepić w jeden string, usuwając \n

ln_pure = [x.strip() for x in ln]
print(ln_pure)
full = ''.join(ln_pure)
print(full)