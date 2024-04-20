from log2 import get_log_2


def test_get_log_2_positive_numbers():
    assert abs(get_log_2(1.0) - 0.0) < 0.001
    assert abs(get_log_2(2.0) - 1.0) < 0.001
    assert abs(get_log_2(4.0) - 2.0) < 0.001
    assert abs(get_log_2(8.0) - 3.0) < 0.001
    assert abs(get_log_2(16.0) - 4.0) < 0.001


def test_get_log_2_small_numbers():
    assert abs(get_log_2(0.5) - (-1.0)) < 0.001
    assert abs(get_log_2(0.25) - (-2.0)) < 0.001
    assert abs(get_log_2(0.125) - (-3.0)) < 0.001


def test_get_log_2_large_numbers():
    assert abs(get_log_2(1024.0) - 10.0) < 0.001
    assert abs(get_log_2(65536.0) - 16.0) < 0.001
    assert abs(get_log_2(16777216.0) - 24.0) < 0.001
