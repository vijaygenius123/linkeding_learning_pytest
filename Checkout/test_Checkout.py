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
