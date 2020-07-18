import pytest

def fizzBuzz(value):
    if value % 3 == 0:
        return "Fizz"
    if value % 5 == 0:
        return "Buzz"
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

def test_returnsBuzzWith5PassedIn():
    checkFizzBuzz(5,"Buzz")

def test_returnsFizzWith6PassedIn():
    checkFizzBuzz(6,"Fizz")

def test_returnsBuzzWith10PassedIn():
    checkFizzBuzz(10,"Buzz")