import json

class RecipeProcessor:
    def __init__(self):
        self.recipes = []

    def load_recipes(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)
            for entry in data['recipes']:
                recipe = Recipe(entry['name'], entry['cookTime'], entry['prepTime'], entry['recipeYield'], entry['imageUrl'])
                self.recipes.append(recipe)

    def get_recipes(self):
        return self.recipes
