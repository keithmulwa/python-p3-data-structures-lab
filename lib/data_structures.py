spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    # Return a list of names
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    # Return foods with heat_level > 5
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    # Print all foods in the required format
    for food in spicy_foods:
        peppers = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {peppers}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # Return the first food matching the given cuisine
    return next(food for food in spicy_foods if food["cuisine"] == cuisine)

def print_spiciest_foods(spicy_foods):
    # Print only the spiciest foods (heat_level > 5)
    for food in get_spiciest_foods(spicy_foods):
        peppers = "🌶" * food["heat_level"]
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {peppers}')

def get_average_heat_level(spicy_foods):
    # Return the integer average heat level
    total = sum(food["heat_level"] for food in spicy_foods)
    return total // len(spicy_foods)

def create_spicy_food(spicy_foods, spicy_food):
    # Add new food to the list and return it
    spicy_foods.append(spicy_food)
    return spicy_foods
