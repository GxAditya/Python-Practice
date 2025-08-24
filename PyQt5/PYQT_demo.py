"""
pyqt5_demo.py

This script demonstrates the basics of PyQt5:
1. Creating a main application window
2. Adding widgets (Label, Button, Text Input)
3. Connecting signals to slots (event handling)
4. Running the application

What is PyQt5?
--------------
- PyQt5 is a set of Python bindings for the Qt application framework.
- It allows you to create cross-platform desktop applications with a native look and feel.
- Works on Windows, macOS, and Linux.

Installation:
-------------
pip install PyQt5
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

# ---------------------------
# Main Window Class
# ---------------------------

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("PyQt5 Demo App")
        self.setGeometry(100, 100, 300, 200)  # x, y, width, height

        # Create widgets
        self.label = QLabel("Enter your name:", self)
        self.text_input = QLineEdit(self)
        self.button = QPushButton("Greet Me", self)
        self.output_label = QLabel("", self)

        # Connect button click to function
        self.button.clicked.connect(self.greet_user)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.text_input)
        layout.addWidget(self.button)
        layout.addWidget(self.output_label)

        self.setLayout(layout)

    # ---------------------------
    # Slot (Event Handler)
    # ---------------------------
    def greet_user(self):
        """Gets text from input and updates the output label."""
        name = self.text_input.text().strip()
        if name:
            self.output_label.setText(f"Hello, {name}!")
        else:
            self.output_label.setText("Please enter your name.")

# ---------------------------
# Application Entry Point
# ---------------------------

if __name__ == "__main__":
    # Every PyQt5 app needs a QApplication instance
    app = QApplication(sys.argv)

    # Create and show the main window
    window = MyWindow()
    window.show()

    # Start the event loop
    sys.exit(app.exec_())