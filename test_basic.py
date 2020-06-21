import pytest

@pytest.fixture
def setup():
    print("Setup")

# will run as a test
def test_basic(setup):
    print("Running Test")
    assert True

# will run as a test
def test_func():
    print("Running Test Func")
    assert True