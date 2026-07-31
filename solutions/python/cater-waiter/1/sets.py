"""Functions for compiling dishes and ingredients for a catering company."""


from sets_categories_data import (VEGAN,
                                  VEGETARIAN,
                                  KETO,
                                  PALEO,
                                  OMNIVORE,
                                  ALCOHOLS,
                                  SPECIAL_INGREDIENTS)


def clean_ingredients(dish_name, dish_ingredients):
    """Remove duplicates from `dish_ingredients"""
    # Convert the list into a set to automatically drop duplicates
    unique_ingredients = set(dish_ingredients)
    return (dish_name, unique_ingredients)

from sets_categories_data import ALCOHOLS

def check_drinks(drink_name, drink_ingredients):
    """Check if a drink is a cocktail or a mocktail."""
    if set(drink_ingredients).isdisjoint(ALCOHOLS):
        return f"{drink_name} Mocktail"
    else:
        return f"{drink_name} Cocktail"

from sets_categories_data import VEGAN, VEGETARIAN, PALEO, KETO, OMNIVORE


def categorize_dish(dish_name, dish_ingredients):
    """Categorize a dish into a diet type."""
    dish_set = set(dish_ingredients)
    # Check if all dish ingredients belong indide a diet's set
    if dish_set.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif dish_set.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif dish_set.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif dish_set.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"

from sets_categories_data import SPECIAL_INGREDIENTS

def tag_special_ingredients(dish):
   """Find allergens in a dish"""
   dish_name, ingredients_list = dish
   allergens_found = set(ingredients_list) & SPECIAL_INGREDIENTS
   return (dish_name, allergens_found)

def compile_ingredients(dishes):
    """Combine ingredients from multiple dishes into a single master set."""
    return set.union(*dishes)

def separate_appetizers(dishes, appetizers):
    """Remove appetizers from the list of dishes"""
    main_courses = set(dishes) - set(appetizers)
    return list(main_courses)


def singleton_ingredients(dishes, intersection):
    """Find rare ingredients that appear only in one dish."""
    all_ingredients = set.union(*dishes)
    return all_ingredients - intersection
    
