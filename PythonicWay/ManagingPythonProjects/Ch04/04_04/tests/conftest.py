import pytest
import sqlite3


@pytest.fixture
def database():
    conn = sqlite3.connect(':memory:')  # In memory database
    yield conn
    # Cleanup code
    conn.close()
