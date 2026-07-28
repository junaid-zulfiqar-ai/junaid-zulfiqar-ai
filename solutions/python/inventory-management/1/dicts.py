"""Functions to keep track and alter inventory."""


def create_inventory(items):
    """Create a dict that tracks the amount (count) of each element on the `items` list."""
    inventory = {}
    
    for item in items:
        # If the item exists, get its current count. If not, default to 0. Then add 1.
        inventory[item] = inventory.get(item, 0) + 1

    return inventory    

def add_items(inventory, items):
    # Pick up one item at a time from the new box
    for item in items:
            if item in inventory:
                inventory[item] = inventory[item] + 1
            else:
                 inventory[item] = 1
    return inventory    

def decrement_items(inventory, items):
    for item in items:
       if item in inventory:
           if inventory[item] > 0:
               inventory[item] = inventory[item] - 1
    return inventory          

def remove_item(inventory, item):
    if item in inventory:
        del inventory[item]
    return inventory    

def list_inventory(inventory):
    final_report = []
    for item in inventory:
        if inventory[item] > 0:
            pair = (item, inventory[item])
            final_report.append(pair)
    return final_report        