"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart."""
    for item in items_to_add:
        # .get() fetches the current count, or default it to 0 if it's not in the cart yet
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart    


def read_notes(notes):
    """"Create a shoppng cart from a list of notes."""
    # Takes the 'notes' iterable and makes every item a key with the value 1
    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary with new recipes."""
    # .update() unpacks the new recipes and merges them straight into our ideas dict
    ideas.update(recipe_updates)

    return ideas


def sort_entries(cart):
    """Sort a shopping cart alphabetically."""
    # .items() gets all the key-value pairs, sorted() alphabetizes them by key
    return dict(sorted(cart.items()))


def send_to_store(cart, aisle_mapping):
    """Comine user cart with store location data in reverse alphabetical order."""
    fulfillment_cart = {}
    for item in sorted(cart.keys(), reverse=True):
        quantity_as_list = [cart[item]]
        location_list = aisle_mapping[item]
        fulfillment_cart[item] = quantity_as_list + location_list

    return fulfillment_cart


def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
        customer_quantity = fulfillment_cart[item][0]
        current_shelf_count = store_inventory[item][0]
        new_count = current_shelf_count - customer_quantity
        if new_count == 0:
            store_inventory[item][0] = "Out of Stock"
        else:
            store_inventory[item][0] = new_count

    return store_inventory        
