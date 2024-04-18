import json
from Recipe import Recipe


class RecipeProcessor:
    def __init__(self):
        self._recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            for entry in data:
                recipe = Recipe(entry['name'], entry['cookTime'], entry['prepTime'], entry['recipeYield'],
                                entry['description'], entry['ingredients'], entry['image'])
                self._recipes.append(recipe)

    def get_recipes(self):
        return self._recipes
