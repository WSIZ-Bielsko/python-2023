import matplotlib.pyplot as plt     # tą bibliotekę można/trzeba doinstalować przez `pip install matplotlib` albo podobnie....


def is_square(a: int) -> bool:
    x = int(a ** 0.5)
    if x * x == a:
        return True
    return False

def get_square_numbers(max_number: int):
    x = []
    y = []
    for a in range(-max_number,max_number+1):
        for b in range(-max_number,max_number+1):
            if a * b == 0:
                continue
            cc = a**2 + b**2
            if is_square(cc):
                # print(a, b, int((a**2+b**2)**0.5))
                x.append(a)
                y.append(b)
    return x, y


if __name__ == '__main__':
    x, y = get_square_numbers(3000)
    plt.scatter(x,y, s=2)
    plt.show()