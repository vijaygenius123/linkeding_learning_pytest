import pytest


@pytest.fixture(autouse=True)
def setup():
    print("\nSetup")

def test_func1():
    print("Running Test 1")
    assert True

def test_func2():
    print("Running Test 2")
    assert True