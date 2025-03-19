#Student B
from item import Item

class Inventory:
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]
    
    def total_inventory_value(self):
        return sum(item.total_cost() for item in self.items)
    
    def __str__(self):
        return "\n".join(str(item) for item in self.items)
