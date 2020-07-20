class Checkout:

    class Discount:

        def __init__(self,quantity,price):
            self.quantity = quantity
            self.price = price


    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}
    
    def addDiscount(self, item,quantity,price):
        discount = self.Discount(quantity,price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item not in self.items:
            raise Exception("Bad Item")
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1


    def calculateTotal(self):
        total = 0
        for item,count in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if count >= discount.quantity:
                    numberOfDiscounts = count / discount.quantity
                    total = numberOfDiscounts * discount.price
                    remaining = count % discount.quantity
                    total += remaining * self.prices[item]
                else:
                    total += self.prices[item]
            else:
                total += self.prices[item] * count
        return total
