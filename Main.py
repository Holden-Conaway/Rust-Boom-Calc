import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

# Crafting recipes dictionary
craftingRecipes = {
    "Satchel Charge": {
        "sulfur": 480,
        "charcoal": 480,
        "metal frags": 80,
        "rope": 1,
        "small stash": 1
    },
    "Explo Ammo": {
        "metal frag": 5,
        "gunpowder": 10,
        "sulfur": 5
    },
    "Rocket": {
        "metal frags": 100,
        "low grade": 30,
        "sulfur": 1400,
        "charcoal": 1400,
        "metal pipe": 2
    },
    "C4": {
        "charcoal": 2000,
        "metal frags": 200,
        "low grade": 60,
        "sulfur": 2200,
        "cloth": 5,
        "tech trash": 2
    }
}

def calcResources(exploType, quantity):
    if exploType not in craftingRecipes:
        return f"Error: That isn't a valid explosive type."

    recipe = craftingRecipes[exploType]
    totalResources = {resource: amount * quantity for resource, amount in recipe.items()}

    result = f"To craft {quantity} {exploType}(s), you need:\n"
    for resource, amount in totalResources.items():
        result += f"- {amount} {resource}\n"

    return result

def checkCraftable(rawResources):
    canCraft = []
    craftable_info = {}

    for item, recipe in craftingRecipes.items():
        # Determine the maximum number of items that can be crafted
        min_items = float('inf')  # Start with an infinite number of possible items
        for resource, amount_needed in recipe.items():
            if resource not in rawResources:
                min_items = 0
                break
            available = rawResources.get(resource, 0)
            possible_items = available // amount_needed
            min_items = min(min_items, possible_items)

        if min_items > 0:
            craftable_info[item] = min_items

    if craftable_info:
        result = "With the provided resources, you can craft the following:\n"
        for item, count in craftable_info.items():
            result += f"- {count} {item}(s)\n"
        return result
    else:
        return "With the provided resources, you cannot craft anything."

class BoomCalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Rust Boom Calculator")
        self.setGeometry(100, 100, 400, 600)

        # Layouts
        main_layout = QVBoxLayout(self)
        form_layout = QVBoxLayout()
        result_layout = QVBoxLayout()  # Separate layout for results
        button_layout = QHBoxLayout()

        # Explosive Type Dropdown
        self.explosive_type_label = QLabel("Select Explosive Type:")
        self.explosive_type_dropdown = QComboBox(self)
        self.explosive_type_dropdown.addItems(craftingRecipes.keys())
        self.explosive_type_dropdown.setCurrentText("Satchel Charge")

        # Quantity Input
        self.quantity_label = QLabel("Enter Quantity:")
        self.quantity_entry = QLineEdit(self)
        self.quantity_entry.setPlaceholderText("Enter quantity")

        # Raw Resources Input
        self.resources_label = QLabel("Enter Your Raw Resources (separate with commas, e.g. sulfur=1000, charcoal=2000):")
        self.resources_entry = QLineEdit(self)
        self.resources_entry.setPlaceholderText("e.g. sulfur=1000, charcoal=2000")

        # Calculate Button
        self.calculate_button = QPushButton("Calculate Resources", self)
        self.calculate_button.clicked.connect(self.on_calculate)

        # Quit Button
        self.quit_button = QPushButton("Quit", self)
        self.quit_button.clicked.connect(self.close)

        # Result Text Box
        self.result_text = QTextEdit(self)
        self.result_text.setReadOnly(True)
        self.result_text.setPlaceholderText("Results will be shown here...")

        # Add widgets to form layout
        form_layout.addWidget(self.explosive_type_label)
        form_layout.addWidget(self.explosive_type_dropdown)
        form_layout.addWidget(self.quantity_label)
        form_layout.addWidget(self.quantity_entry)
        form_layout.addWidget(self.resources_label)
        form_layout.addWidget(self.resources_entry)
        form_layout.addWidget(self.calculate_button)

        # Add widgets to result layout
        result_layout.addWidget(self.result_text)

        # Add form layout and result layout to main layout
        main_layout.addLayout(form_layout)
        main_layout.addLayout(result_layout)

        # Add quit button to the bottom of the layout
        button_layout.addWidget(self.quit_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

        # Apply styling (QSS)
        self.setStyleSheet("""
            QWidget {
                background-color: #2c3e50;
                color: white;
                font-family: Arial, sans-serif;
            }

            QLabel {
                font-size: 14px;
            }

            QComboBox, QLineEdit, QPushButton, QTextEdit {
                background-color: #34495e;
                color: white;
                border: 2px solid #7f8c8d;
                padding: 5px;
                font-size: 14px;
            }

            QComboBox:hover, QLineEdit:hover, QPushButton:hover, QTextEdit:hover {
                background-color: #1abc9c;
            }

            QPushButton {
                background-color: #e74c3c;
                border-radius: 5px;
                padding: 10px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #c0392b;
            }

            QTextEdit {
                margin-top: 20px;
                font-size: 12px;
                background-color: #ecf0f1;
                color: #2c3e50;
            }

            QPushButton#quit_button {
                background-color: #95a5a6;
            }

            QPushButton#quit_button:hover {
                background-color: #7f8c8d;
            }
        """)

    def on_calculate(self):
        # Get user input for explosive type and quantity
        explosive_type = self.explosive_type_dropdown.currentText()
        try:
            quantity = int(self.quantity_entry.text())
        except ValueError:
            self.show_error("Invalid Input", "Please enter a valid number for quantity.")
            return

        if explosive_type not in craftingRecipes:
            self.show_error("Invalid Explosive", "Please select a valid explosive type.")
            return

        result = calcResources(explosive_type, quantity)

        # Parse raw resources from input
        raw_resources_input = self.resources_entry.text()
        raw_resources = {}

        if raw_resources_input:
            try:
                for entry in raw_resources_input.split(","):
                    resource, amount = entry.split("=")
                    raw_resources[resource.strip()] = int(amount.strip())
            except ValueError:
                self.show_error("Invalid Input", "Please enter the resources in the correct format.")
                return

            # Check how many items can be crafted based on raw resources
            craftable_result = checkCraftable(raw_resources)
            result += "\n\n" + craftable_result

        self.result_text.setPlainText(result)

    def show_error(self, title, message):
        QMessageBox.critical(self, title, message)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BoomCalculatorApp()
    window.show()
    sys.exit(app.exec_())
