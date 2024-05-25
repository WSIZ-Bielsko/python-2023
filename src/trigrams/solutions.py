def get_trigrams(s: str) -> list[str]:
    x = '  ' + s.strip() + ' '
    result = []
    for start in range(len(x) - 2):
        result.append(x[start: start + 3])
    return result


def simple_trigram_similarity(w1: str, w2: str) -> float:
    t1 = set(get_trigrams(w1))
    t2 = set(get_trigrams(w2))
    common = len(t1 & t2)
    in_any_of_both = len(t1 | t2)
    return common / in_any_of_both
