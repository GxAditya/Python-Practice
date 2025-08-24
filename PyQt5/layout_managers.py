"""
PyQt5 Layout Managers - Detailed Guide with Examples
----------------------------------------------------
This script demonstrates how to use different layout managers in PyQt5:
    1. QVBoxLayout  - Vertical stacking of widgets
    2. QHBoxLayout  - Horizontal stacking of widgets
    3. QGridLayout  - Grid-based positioning
    4. QFormLayout  - Label–field pairing
    5. Nested Layouts - Combining layouts for complex UIs

Run:
    pip install PyQt5
    python pyqt5_layouts_demo.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QLineEdit,
    QTextEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QFormLayout
)
from PyQt5.QtCore import Qt


class LayoutDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Layout Managers - Detailed Demo")
        self.setGeometry(200, 200, 600, 500)

        # Call the method to build UI
        self.init_ui()

    def init_ui(self):
        """
        Create and arrange widgets using different layout managers.
        We'll nest them inside a main vertical layout.
        """

        # ---------------------------
        # 1. VBox Layout Example
        # ---------------------------
        vbox_section_label = QLabel("1. QVBoxLayout Example")
        vbox_section_label.setStyleSheet("font-weight: bold;")

        vbox_layout = QVBoxLayout()
        vbox_layout.addWidget(QPushButton("Button 1"))
        vbox_layout.addWidget(QPushButton("Button 2"))
        vbox_layout.addWidget(QPushButton("Button 3"))

        # Add stretch to push last button to bottom
        vbox_layout.addStretch()

        # ---------------------------
        # 2. HBox Layout Example
        # ---------------------------
        hbox_section_label = QLabel("2. QHBoxLayout Example")
        hbox_section_label.setStyleSheet("font-weight: bold;")

        hbox_layout = QHBoxLayout()
        hbox_layout.addWidget(QPushButton("Left"))
        hbox_layout.addStretch()  # Pushes next widget to the right
        hbox_layout.addWidget(QPushButton("Right"))

        # ---------------------------
        # 3. Grid Layout Example
        # ---------------------------
        grid_section_label = QLabel("3. QGridLayout Example")
        grid_section_label.setStyleSheet("font-weight: bold;")

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Row 0, Col 0"), 0, 0)
        grid_layout.addWidget(QLabel("Row 0, Col 1"), 0, 1)
        grid_layout.addWidget(QLabel("Row 1, Col 0"), 1, 0)
        grid_layout.addWidget(QLabel("Row 1, Col 1"), 1, 1)
        grid_layout.addWidget(QPushButton("Span 2 cols"), 2, 0, 1, 2)  # Row 2, Col 0, span 1 row, 2 cols

        # ---------------------------
        # 4. Form Layout Example
        # ---------------------------
        form_section_label = QLabel("4. QFormLayout Example")
        form_section_label.setStyleSheet("font-weight: bold;")

        form_layout = QFormLayout()
        form_layout.addRow("Name:", QLineEdit())
        form_layout.addRow("Email:", QLineEdit())
        form_layout.addRow("Bio:", QTextEdit())

        # ---------------------------
        # 5. Nested Layout Example
        # ---------------------------
        nested_section_label = QLabel("5. Nested Layout Example")
        nested_section_label.setStyleSheet("font-weight: bold;")

        # Inner horizontal layout
        inner_hbox = QHBoxLayout()
        inner_hbox.addWidget(QPushButton("Nested Left"))
        inner_hbox.addWidget(QPushButton("Nested Right"))

        # Outer vertical layout containing the inner horizontal layout
        nested_vbox = QVBoxLayout()
        nested_vbox.addWidget(QLabel("Above Nested HBox"))
        nested_vbox.addLayout(inner_hbox)
        nested_vbox.addWidget(QLabel("Below Nested HBox"))

        # ---------------------------
        # Main Layout (Vertical)
        # ---------------------------
        main_layout = QVBoxLayout()

        # Add each section to the main layout
        main_layout.addWidget(vbox_section_label)
        main_layout.addLayout(vbox_layout)

        main_layout.addSpacing(15)  # Space between sections
        main_layout.addWidget(hbox_section_label)
        main_layout.addLayout(hbox_layout)

        main_layout.addSpacing(15)
        main_layout.addWidget(grid_section_label)
        main_layout.addLayout(grid_layout)

        main_layout.addSpacing(15)
        main_layout.addWidget(form_section_label)
        main_layout.addLayout(form_layout)

        main_layout.addSpacing(15)
        main_layout.addWidget(nested_section_label)
        main_layout.addLayout(nested_vbox)

        # Set the main layout for the window
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LayoutDemo()
    demo.show()
    sys.exit(app.exec_())