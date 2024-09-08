class PolynomialRollingHash:
    def __init__(self, p=31, m=10 ** 9 + 9, hash_length=6):
        self.p = p
        self.m = m
        self.p_pow = [1]
        self.hash_length = hash_length
        self.calculate_powers(max_length=30)

    def calculate_powers(self, max_length):
        while len(self.p_pow) < max_length:
            self.p_pow.append((self.p_pow[-1] * self.p) % self.m)

    def hash(self, s):
        hash_value = 0
        for i, char in enumerate(s):
            if i >= self.hash_length:
                break
            val = ord(char) - ord('a') + 1
            hash_value = (hash_value + val * self.p_pow[self.hash_length - 1 - i]) % self.m
        return hash_value

    def roll_hash(self, old_hash, old_char, new_char, length):
        old_val = ord(old_char) - ord('a') + 1
        new_val = ord(new_char) - ord('a') + 1
        new_hash = (old_hash - old_val * self.p_pow[length - 1]) % self.m
        new_hash = (new_hash * self.p + new_val) % self.m
        return new_hash


if __name__ == '__main__':
    s = 'loremipsumdolorsitamet'
    LEN = 3
    ph = PolynomialRollingHash(hash_length=LEN)

    START = 5  # want hash starting there

    # direct way
    print(ph.hash(s[START:]))

    # rolling way
    h = ph.hash(s[0:])
    for start in range(1, START + 1):
        oc = s[start - 1]
        nc = s[start + LEN - 1]
        print(oc, nc)
        h = ph.roll_hash(old_hash=h, old_char=oc, new_char=nc, length=LEN)
    # end: hash with first char at 5
    print(h)
