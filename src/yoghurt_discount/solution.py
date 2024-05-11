def find_best_purchase(n: int, a: int, b: int) -> int:
    if 2 * a > b:
        if n % 2 == 0:
            return n * b // 2
        else:
            return (n - 1) * b // 2 + a
    else:
        return n * a


# def find_best_purchase(n: int, a: int, b: int) -> int:
#     if n % 2 == 0:
#         return min(a * n, b * n//2)
#     else:
#         n -= 1
#         return a + min(a * n, b * n//2)
