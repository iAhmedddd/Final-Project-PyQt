import requests
from PyQt5.QtGui import QPixmap

class Recipe:
    def __init__(self, name, cook_time, prep_time, recipe_yield, image_url):
        self.name = name
        self.cook_time = cook_time
        self.prep_time = prep_time
        self.recipe_yield = recipe_yield
        self.image_url = image_url
        self.image_filename = ""

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
        # Image download logic with progress bar
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(self.image_filename, 'wb') as f:
                f.write(response.content)
            print(f"! Downloading image {self.image_filename}")
        else:
            print(f"Failed to download {url}")

    def get_image(self):
        return self.image_filename