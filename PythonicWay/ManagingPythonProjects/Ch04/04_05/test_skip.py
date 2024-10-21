from os import environ

import pytest

is_ci = 'CI' in environ


@pytest.mark.skipif(not is_ci, reason='not in CI environment')
def test_that_requires_ci():
    print('CI test')  # TODO: Write actual test
