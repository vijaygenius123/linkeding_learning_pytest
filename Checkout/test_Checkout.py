import pytest
from Checkout import Checkout

"""
    ✔ Can Create An Instance Of Checkout class
    ☐ Can add item price
    ☐ Can add an item
    ☐ Can calculate current total price
    ☐ Can add multiple items and get correct total price
    ☐ Can add discount rules
    ☐ Can apply discount rules to total
    ☐ Exception is thrown if item is added without price
"""

@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout

def test_canAddItemPrice(checkout):
    checkout.addItemPrice("Test",1)

def test_canAddItem(checkout):
    checkout.addItem("Test")

def test_canCalculateTotal(checkout):
    checkout.addItemPrice("Test",1)
    checkout.addItem("Test")
    assert checkout.calculateTotal() == 1


def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItemPrice("Milk",1)
    checkout.addItemPrice("Bread",2)
    checkout.addItem("Milk")
    checkout.addItem("Bread")
    assert checkout.calculateTotal() == 3