import time

import requests
from time import sleep


class Recipe:
    def __init__(self, name, cook_time, prep_time, recipe_yield, description, ingredients):
        self.name = name
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.recipe_yield = recipe_yield
        self.image_filename = ""
        self.description = description
        self.ingredients = ingredients

    def get_name(self):
        return self.name

    def get_cook_time(self):
        return self.format_time(self.cook_time)

    def get_prep_time(self):
        return self.format_time(self.prep_time)

    def get_recipe_yield(self):
        return self.recipe_yield

    def format_time(self, time):
        # Assuming time is in minutes for simplicity
        hours, minutes = divmod(time, 60)
        return f"{hours:02}:{minutes:02}"

    def set_image(self, url):
        slash = url.rfind('/')
        if slash != -1:
            # Extract the substring after the last '/'
            self.image_filename = url[slash + 1:]
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                with open(self.image_filename, 'wb') as f:
                    f.write(response.content)
        except requests.exceptions.RequestException as e:
            pass

    def get_image(self):
        return self.image_filename
