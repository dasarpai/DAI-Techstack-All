import pytest

import mathlib


def test_sqrt():
    n = 2
    expected = 1.4142
    value = mathlib.sqrt(n)
    assert expected == round(value, 4), f'sqrt({n})'


sqrt_cases = [
    (1, 1),
    (2, 1.4142),
    (4, 2),
]


@pytest.mark.parametrize('n, expected', sqrt_cases)
def test_sqrt_many(n, expected):
    value = mathlib.sqrt(n)
    assert expected == round(value, 4), f'sqrt({n})'
