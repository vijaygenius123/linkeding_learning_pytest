import pytest

def fizzBuzz(value):
    if value == 3:
        return "Fizz"
    return str(value)



def checkFizzBuzz(value, expected):
    retval = fizzBuzz(value)
    assert retval == expected

def test_canCallFizzBuzz():
    fizzBuzz(1)

def test_returns1With1PassedIn():
    checkFizzBuzz(1,"1")


def test_returns2With2PassedIn():
    checkFizzBuzz(2,"2")

def test_returnsFizzWith3PassedIn():
    checkFizzBuzz(3,"Fizz")