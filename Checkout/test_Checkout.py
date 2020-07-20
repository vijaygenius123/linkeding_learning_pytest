import pytest
from Checkout import Checkout

"""
    ✔ Can Create An Instance Of Checkout class @done(20-07-19 20:04)
    ✔ Can add item price @done(20-07-19 20:29)
    ✔ Can add an item @done(20-07-19 20:29)
    ✔ Can calculate current total price @done(20-07-19 20:29)
    ✔ Can add multiple items and get correct total price @done(20-07-19 20:29)
    ☐ Can add discount rules
    ☐ Can apply discount rules to total
    ☐ Exception is thrown if item is added without price
"""

@pytest.fixture()
def checkout():
    checkout = Checkout()
    checkout.addItemPrice("Milk",1)
    checkout.addItemPrice("Bread",2)
    return checkout

def test_canCalculateTotal(checkout):
    checkout.addItem("Milk")
    assert checkout.calculateTotal() == 1

def test_getCorrectTotalWithMultipleItems(checkout):
    checkout.addItem("Milk")
    checkout.addItem("Bread")
    assert checkout.calculateTotal() == 3

def test_canAddDiscountRules(checkout):
    checkout.addDiscount("Milk",3,2)

def test_canApplyDiscountRules(checkout):
    checkout.addDiscount("Milk",3,2)
    checkout.addItem("Milk")
    checkout.addItem("Milk")
    checkout.addItem("Milk")
    assert checkout.calculateTotal() == 2