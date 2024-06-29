def sum_of_chars(s: str) -> int:
    # zsumować ord wszystkich znaków napisu "s", pomnożonych przez ich pozycję w tym napisie
    # przykład:
    # s = 'abc' ->
    # res = 97 * 1 + 98 * 2 + 99 * 3 --> 590
    res = 0
    for i in range(len(s)):
        res += (i + 1) * ord(s[i])
    return res % 107


def polynomial_hash(s, p=31, m=10 ** 9 + 9):
    hash_value = 0
    p_pow = 1

    for char in s:
        hash_value = (hash_value + (ord(char) - ord('a') + 1) * p_pow) % m
        p_pow = (p_pow * p) % m

    return hash_value


if __name__ == '__main__':
    s = 'abrakadabra'
    # s = 'loremipsumdolorsitametconsecteturloremipsumdolorsitametconsecteturloremipsumdolorsitametconsecteturloremipsumdolorsitametconsectetur'
    for c in s:
        print(c, ord(c), chr(ord(c)))

    print(polynomial_hash(s))
    print(polynomial_hash(s+','))
    print(polynomial_hash(s+'.'))
