from amoeba import *


def test_trivial():
    assert get_final_amoeba_size(init_size=1, food=[0, 0, 0]) == 1
    assert get_final_amoeba_size(init_size=1, food=[1]) == 2
    assert get_final_amoeba_size(init_size=1, food=[1, 1, 1]) == 2


def test_basic():
    assert get_final_amoeba_size(init_size=2, food=[2, 3, 4, 5, 6, 7]) == 8
    assert get_final_amoeba_size(init_size=1, food=[2, 3, 4, 5, 6, 7]) == 1
    assert get_final_amoeba_size(init_size=3, food=[2, 3, 4, 5, 6, 7]) == 12
    assert get_final_amoeba_size(init_size=5, food=[2, 3, 4, 5, 6, 7]) == 10
