from src.yoghurt_discount.solution import find_best_purchase


def test_simple():
    assert find_best_purchase(1, 10, 15) == 10
    assert find_best_purchase(2, 10, 15) == 15


def test_discord():
    assert find_best_purchase(4, 3, 5) == 10
    assert find_best_purchase(5, 3, 5) == 13
    assert find_best_purchase(4, 3, 10) == 12
    assert find_best_purchase(5, 3, 10) == 15
