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
    names = []
    for i in range(0,len(spicy_foods)):
        names.append(spicy_foods[i]["name"])
    return names

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for i in range(0,len(spicy_foods)):
        if (spicy_foods[i]["heat_level"]) > 5 :
            spiciest_foods.append(spicy_foods[i])
    return spiciest_foods

def print_spicy_foods(spicy_foods):
    for i in range(0,len(spicy_foods)):
        print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {"🌶" * spicy_foods[i]["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for i in range(0,len(spicy_foods)):
        if cuisine == (spicy_foods[i]["cuisine"]):
            return (spicy_foods[i])

def print_spiciest_foods(spicy_foods):
    for i in range(0,len(spicy_foods)):
        if (spicy_foods[i]["heat_level"]) > 5 :
            print(f'{spicy_foods[i]["name"]} ({spicy_foods[i]["cuisine"]}) | Heat Level: {"🌶" * spicy_foods[i]["heat_level"]}')

def get_average_heat_level(spicy_foods):
    h = []
    for i in range(0,len(spicy_foods)):
        h.append(spicy_foods[i]["heat_level"])
    return sum(h) / len(h)

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods
