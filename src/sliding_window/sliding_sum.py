from datetime import datetime
from random import randint, seed


def gen_network_traffic(n_packets: int) -> list[int]:
    return [randint(0, 10) for _ in range(n_packets)]


def get_the_highest_sum_of_traffic(network_traffics: list[int]) -> int:
    max_sum = 0
    for i in range(len(network_traffics) - 3599):
        current_sum = sum(network_traffics[i:i + 3600])
        max_sum = max(max_sum, current_sum)

    return max_sum


def get_the_highest_sum_of_traffic_2(packets: list[int]) -> int:
    current_sum = sum(packets[:3600])
    max_sum = current_sum

    for start in range(1, len(packets) - 3599):
        current_sum = current_sum - packets[start - 1] + packets[start + 3599]
        max_sum = max(max_sum, current_sum)

    return max_sum


def ts():
    return datetime.now().timestamp()


if __name__ == '__main__':
    seed(111)
    data = gen_network_traffic(n_packets=24 * 3600)
    print(sum(data))
    st = ts()
    res = get_the_highest_sum_of_traffic_2(data)
    en = ts()
    print(res)
    print(f'execution time: {en - st:.3f}s')
