import json
from Recipe import Recipe


class RecipeProcessor:
    def __init__(self):
        self._recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            Recipe.recipes = len(data)
            for index, entry in enumerate(data):
                recipe = Recipe(entry['name'], entry['cookTime'], entry['prepTime'], entry['recipeYield'],
                                entry['description'], entry['ingredients'], len(data))
                self._recipes.append(recipe)
                recipe.set_image(entry['image'], index)

    def get_recipes(self):
        return self._recipes
