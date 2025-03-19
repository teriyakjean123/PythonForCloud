#Student C
from item import Item
from inventory import Inventory

def test_inventory_system():
    item1 = Item("Laptop", 1000, 2)
    item2 = Item("Mouse", 50, 5)
    item3 = Item("Keyboard", 80, 3)
    
    inventory = Inventory()
    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)
    
    print("Inventory System Test:")
    print(inventory)
    print(f"Total Inventory Value: ${inventory.total_inventory_value()}")
    
    # If you want to remove an item just change the item name you want to remove.
    inventory.remove_item("Mouse")
    print("\nAfter removing Mouse:")
    print(inventory)
    print(f"Total Inventory Value: ${inventory.total_inventory_value()}")

    