#Student A
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name}: ${self.price} x {self.quantity} = ${self.total_cost()}"

