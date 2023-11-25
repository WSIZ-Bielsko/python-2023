def is_square(a: int) -> bool:
    x = int(a ** 0.5)
    if x * x == a:
        return True
    return False


