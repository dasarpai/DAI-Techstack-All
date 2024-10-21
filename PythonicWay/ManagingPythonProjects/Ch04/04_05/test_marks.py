from time import sleep

import pytest


def test_anytime():
    print('anytime')  # TODO: Write test code


@pytest.mark.slow
def test_slow():
    sleep(1)  # Simulate work
    print('slow')  # TODO: Write test code
