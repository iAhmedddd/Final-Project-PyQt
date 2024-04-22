import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from RecipeProcessor import RecipeProcessor  

class RecipeUI(QWidget):
    def __init__(self):
        super().__init__()  
        self.processor = RecipeProcessor('recipes.json')
        self.current_index = 0
        self.setup_window()
        self.layout_ui(self.processor.get_recipes())

    def setup_window(self):
        self.setWindowTitle("Recipe Viewer")
        self.setGeometry(100, 100, 800, 600)  # Set initial size and position

    def layout_ui(self, recipes):
        self.layout = QVBoxLayout(self)
        self.grid = QGridLayout()
        self.layout.addLayout(self.grid)
        self.update_grid(recipes[:4])  # showing the first four recipes

        # Navigation buttons
        nav_buttons = QHBoxLayout()
        self.prev_button = QPushButton("Previous")
        self.prev_button.clicked.connect(self.previous)
        nav_buttons.addWidget(self.prev_button)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.next)
        nav_buttons.addWidget(self.next_button)

        self.layout.addLayout(nav_buttons)

def update_grid(self, recipes):
        for i in reversed(range(self.grid.count())):
            widget = self.grid.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        for i, recipe in enumerate(recipes):
            row, col = divmod(i, 2)
            label = QLabel(f"{recipe.name}\nCook Time: {recipe.get_cook_time()}\nPrep Time: {recipe.get_prep_time()}")
            self.grid.addWidget(label, row * 2, col)
            if recipe.get_image():
                pixmap = QPixmap(recipe.get_image())
                image_label = QLabel()
                image_label.setPixmap(pixmap.scaled(200, 200, Qt.KeepAspectRatio))
                self.grid.addWidget(image_label, row * 2 + 1, col)

    def first(self):
        self.current_index = 0
        self.display_recipes()

    def last(self):
        self.current_index = max(0, len(self.processor.get_recipes()) - 4)
        self.display_recipes()

    def next(self):
        if self.current_index + 4 < len(self.processor.get_recipes()):
            self.current_index += 4
            self.display_recipes()

    def previous(self):
        if self.current_index > 0:
            self.current_index -= 4
            self.display_recipes()

def main():
    app = QApplication(sys.argv)
    ui = RecipeUI()
    ui.show()
    app.exec_()

if __name__ == '__main__':
    main()
