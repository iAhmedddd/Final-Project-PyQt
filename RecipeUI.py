import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from RecipeProcessor import RecipeProcessor  

class RecipeUI(QWidget):
    def __init__(self, recipes):
        super().__init__()
        self.recipes = recipes
        self.current_page = 0
        self.recipes_per_page = 12  # Adjust number of recipes per page as needed
        self.displayed_recipes = self.recipes[:self.recipes_per_page]
        self.setup_window()
        self.layout_ui()

    def setup_window(self):
        self.setWindowTitle("Recipe Viewer")
        self.setGeometry(100, 100, 800, 600)  # Set initial size and position
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.update_ui()

    def update_ui(self):
        self.layout.clear()
        for recipe in self.displayed_recipes:
            label = QLabel(recipe.get_name())
            button = QPushButton('View Recipe')
            self.layout.addWidget(label)
            self.layout.addWidget(button)
        self.add_navigation_buttons()

    # Implement the rest of the methods for navigation and search
    def add_navigation_buttons(self):
        nav_layout = QHBoxLayout()
        first_btn = QPushButton('First')
        first_btn.clicked.connect(self.first)
        previous_btn = QPushButton('Previous')
        previous_btn.clicked.connect(self.previous)
        next_btn = QPushButton('Next')
        next_btn.clicked.connect(self.next)
        last_btn = QPushButton('Last')
        last_btn.clicked.connect(self.last)
        nav_layout.addWidget(first_btn)
        nav_layout.addWidget(previous_btn)
        nav_layout.addWidget(next_btn)
        nav_layout.addWidget(last_btn)
        self.layout.addLayout(nav_layout)

    def previous(self):
        if self.current_page > 0:
            self.current_page -= 1
            start_index = self.current_page * self.recipes_per_page
            end_index = start_index + self.recipes_per_page
            self.displayed_recipes = self.recipes[start_index:end_index]
            self.update_ui()

    def first(self):
        self.current_page = 0
        self.displayed_recipes = self.recipes[:self.recipes_per_page]
        self.update_ui()

    def last(self):
        total_pages = len(self.recipes) // self.recipes_per_page
        self.current_page = total_pages
        start_index = self.current_page * self.recipes_per_page
        self.displayed_recipes = self.recipes[start_index:start_index + self.recipes_per_page]
        self.update_ui()

    def search(self, search_query):
        self.displayed_recipes = [recipe for recipe in self.recipes if
                                  search_query.lower() in recipe.get_name().lower()]
        self.current_page = 0
        self.update_ui()

    def reset(self):
        self.displayed_recipes = self.recipes[:self.recipes_per_page]
        self.current_page = 0
        self.update_ui()

def main():
    app = QApplication([])
    processor = RecipeProcessor()
    processor.load_recipes('recipes.json')
    recipes = processor.get_recipes()       # Retrieve the list of recipes from the processor
    ui = RecipeUI(recipes)                  # Pass the recipes to the UI
    ui.show()
    app.exec_()

if __name__ == '__main__':
    main()
