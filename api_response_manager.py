import requests
import json


def single_dish_recipe(dish_name):
    res = requests.get(f"https://www.themealdb.com/api/json/v1/1/search.php?s={dish_name}")
    data = res.json()
    meal_info = {}
    ingredients = []
    measures = []

    for meal in data["meals"]:
        for k, v in meal.items():
            if 'strMeal' in k and not 'Thumb' in k: meal_info["Name"] = v

            # print(k, v)
            if 'Ingredient' in k and v != '': ingredients.append(v)
            if 'Measure' in k and v != '': measures.append(v)
        abc = []
        print(len(measures))
        print(len(ingredients))
        for measure in measures:
            for ingriedient in ingredients:
                combine = f"{measure} {ingriedient}"
                abc.append(combine)
        # meal_info["Ingredients"] = abc
        print(meal_info)


single_dish_recipe('spaghetti')
