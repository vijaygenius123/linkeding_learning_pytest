
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
def test_canInstantiateCheckout():
    co = Checkout()