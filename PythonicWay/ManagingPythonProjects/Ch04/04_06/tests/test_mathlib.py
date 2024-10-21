import pytest

import mathlib


def test_neg():
    with pytest.raises(ValueError):
        mathlib.sqrt(-2)
