import sys

import requests
from PyQt5.QtGui import QPixmap
import urllib


class Recipe:
    def __init__(self, name, cook_time, prep_time, recipe_yield, description, ingredients, total):
        self.name = name
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.recipe_yield = recipe_yield
        self.image = None
        self.image_filename = ""
        self.description = description
        self.ingredients = ingredients
        self.total = total

    def get_name(self):
        return self.name

    def get_cook_time(self):
        hours, minutes = divmod(self.cook_time, 60)
        return f"{hours:02}:{minutes:02}"

    def get_prep_time(self):
        hours, minutes = divmod(self.prep_time, 60)
        return f"{hours:02}:{minutes:02}"

    def get_recipe_yield(self):
        return self.recipe_yield
        
    def set_image(self, url, index):
        slash = url.rfind('/')
        if slash != -1:
            # Extract the substring after the last '/' to get the name of the file in the url
            self.image_filename = url[slash + 1:]

        # Checking for valid urls 
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(self.image_filename, 'wb') as f:
                    print(f'/ Validating Recipe image {index + 1} of {self.total}')
        except requests.exceptions.RequestException as e:
            pass

    def get_image(self):
        return self.image_filename
