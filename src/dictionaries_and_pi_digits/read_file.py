with open('pi.txt') as f:
    lines = f.readlines()

# print(lines)

lines_pure = [x.strip() for x in lines]
pi_string = ''.join(lines_pure)
print(pi_string)

