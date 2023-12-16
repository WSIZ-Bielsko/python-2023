import unittest


def set_boiler_power(current_temp: float, desired_temp: float, max_power: float, temperature_window: float) -> float:
    """
    Funkcja obliczająca moc urządzenia grzewczego w zależności od aktualnej temepeatury (current_temp),
    wymaganej temperatury (desired_temp), i maksymalnej mocy pieca (max_power);

    Zasada działania:
    1) jeśli current_temp > desired_temp --- moc ma być 0 (return == 0)
    2) jeśli current_temp < desired_temp -- piec ma grzać... czyli return > 0
    3) jeśli current_temp < desired_temp - temperature_window -- piec ma grzać z maksymalną mocą (max_power)
    4) w przypadku między 2 i 3 moc pieca ma rosnąć liniowo

    Przykład 1:
    -current_temp = 10C
    -desired_temp = 20C
    -temperature_window = 10C
    -max_power = 10
    - --> return = 10  (akurat od tej temperatury w dół cały czas ma być max_max_power)

    Przykład 2:
    -current_temp = 13.33C
    -desired_temp = 20C
    -temperature_window = 10C
    -max_power = 10
    - --> return = 6.66  (temperatura jest w 1/3 okna temperature_window)

    Przykład 3:
    -current_temp = 19C
    -desired_temp = 20C
    -temperature_window = 10C
    -max_power = 10
    - --> return = 1  (temperatura jest w 1/3 okna temperature_window)

    :return:
    """
    if temperature_window < 0:
        raise ValueError('Temperature window must be positive!')

    if current_temp > desired_temp:
        return 0
    if current_temp < desired_temp - temperature_window:
        return max_power

    in_range = desired_temp - current_temp  # (is > 0 for sure)
    fraction = in_range / temperature_window  # number between 0 and 1

    return fraction * max_power


class TestBoiler(unittest.TestCase):

    def test_basic(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=10, desired_temp=20, max_power=10, temperature_window=10),
                               10, places=3)

    def test_zero(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=21, desired_temp=20, max_power=10, temperature_window=10),
                               0, places=3)

    def test_linear(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=19, desired_temp=20, max_power=10, temperature_window=10),
                               1, places=3)

    def test_linear2(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=18, desired_temp=20, max_power=10, temperature_window=10),
                               2, places=3)

    def test_max2(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=-10, desired_temp=20, max_power=10, temperature_window=10),
                               10, places=3)

    def test_linear3(self):
        self.assertAlmostEqual(set_boiler_power(current_temp=18, desired_temp=20, max_power=1, temperature_window=10),
                               0.2, places=3)

    def test_exception(self):
        with self.assertRaises(ValueError):
            set_boiler_power(10, 20, 10, temperature_window=-5)


if __name__ == '__main__':
    unittest.main()
