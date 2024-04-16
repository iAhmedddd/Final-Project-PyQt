from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class RecipeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.recipes = []
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Recipe Viewer")
        self.setGeometry(100, 100, 800, 600)  # Set initial size and position

    def layout_ui(self, recipes):
        layout = QVBoxLayout()
        for recipe in recipes:
            label = QLabel(recipe.get_name())
            button = QPushButton('View Recipe')
            layout.addWidget(label)
            layout.addWidget(button)
        self.setLayout(layout)

    # Implement the rest of the methods for navigation and search

def main():
    app = QApplication([])
    processor = RecipeProcessor()
    processor.load_recipes('recipes.json')
    ui = RecipeUI()
    ui.layout_ui(processor.get_recipes())
    ui.show()
    app.exec_()

if __name__ == '__main__':
    main()
