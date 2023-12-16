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
    pass
