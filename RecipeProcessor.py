import json
from Recipe import Recipe
from time import sleep
from tqdm import tqdm


class RecipeProcessor:
    def __init__(self):
        self._recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
        for i in tqdm(range(len(data)), desc="Downloading recipe"):
            recipe = Recipe(data[i]['name'], data[i]['cookTime'], data[i]['prepTime'], data[i]['recipeYield'],
                            data[i]['description'], data[i]['ingredients'])
            self._recipes.append(recipe)
            recipe.set_image(data[i]['image'])


    def get_recipes(self):
        return self._recipes
