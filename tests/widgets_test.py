from src.job_scheduler.widgets import get_minimum_screen_count


def test_all_examples():
    with open('widget_test_data.txt', 'r') as f:
        for ln in f.readlines():
            x, y, answer = [int(x) for x in ln.split(' ')]
            # print(x, y)
            assert get_minimum_screen_count(x,y) == answer
