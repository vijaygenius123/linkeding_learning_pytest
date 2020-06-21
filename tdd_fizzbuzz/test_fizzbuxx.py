import pytest

def fizzBuzz(value):
    return str(value)


def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_returns1With1PassedIn():
    retval = fizzBuzz(1)
    assert retval == "1"


def test_returns2With2PassedIn():
    retval = fizzBuzz(2)
    assert retval == "2"