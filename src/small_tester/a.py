with open('words1.csv') as f:
    lines = f.readlines()

print(lines)

all_words = []
for line in lines:
    words = line.split(',')  # -> list[str]
    words[0] = words[0].strip()
    words[1] = words[1].strip()
    all_words.append(words)

print(all_words)  # list[list[str]]


n_words = len(all_words)
for i in range(n_words):
    polish = all_words[i][0]
    enlish = all_words[i][1]
    print(f'para: {polish} - {enlish}')
