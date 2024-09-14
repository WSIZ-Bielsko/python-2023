import math
from concurrent.futures import ProcessPoolExecutor, as_completed
from loguru import logger

def compute_sin(n_iterations, arg: float, idx: int):
    logger.info(f'starting job # {idx}')

    x = arg % (2 * math.pi)
    result = 0
    for n in range(n_iterations):
        term = (-1) ** n * x * (2 * n + 1) * math.sin(2 * n + 1)
        result += term
    logger.info(f'job # {idx} completed')

    return result


def main():
    args = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0]
    n_iterations = 10 ** 7

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(compute_sin, n_iterations, arg, idx) for idx, arg in enumerate(args)]

        for future in as_completed(futures):
            result = future.result()
            print(f"sin(x) ≈ {result:.6f}")



if __name__ == "__main__":
    main()
