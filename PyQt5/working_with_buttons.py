"""
PyQt5 Buttons - Detailed Guide with Examples
--------------------------------------------
This script demonstrates how to work with different types of buttons in PyQt5:
    1. Basic QPushButton
    2. Checkable (toggle) buttons
    3. Connecting signals to slots
    4. Passing arguments with lambda
    5. Grouping buttons with QButtonGroup
    6. Styling buttons with CSS
    7. Enabling/disabling buttons dynamically
    8. Adding icons to buttons

Run:
    pip install PyQt5
    python pyqt5_buttons_demo.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,
    QHBoxLayout, QButtonGroup
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class ButtonDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Buttons - Detailed Demo")
        self.setGeometry(200, 200, 500, 400)

        self.init_ui()

    def init_ui(self):
        """
        Create and arrange different button examples.
        """

        main_layout = QVBoxLayout()

        # ---------------------------
        # 1. Basic QPushButton
        # ---------------------------
        basic_label = QLabel("1. Basic QPushButton")
        basic_label.setStyleSheet("font-weight: bold;")

        basic_btn = QPushButton("Click Me")
        basic_btn.clicked.connect(self.on_basic_click)

        main_layout.addWidget(basic_label)
        main_layout.addWidget(basic_btn)

        # ---------------------------
        # 2. Checkable (Toggle) Button
        # ---------------------------
        toggle_label = QLabel("2. Checkable (Toggle) Button")
        toggle_label.setStyleSheet("font-weight: bold;")

        toggle_btn = QPushButton("Toggle Me")
        toggle_btn.setCheckable(True)  # Makes it toggleable
        toggle_btn.toggled.connect(self.on_toggle)

        main_layout.addWidget(toggle_label)
        main_layout.addWidget(toggle_btn)

        # ---------------------------
        # 3. Passing Arguments with Lambda
        # ---------------------------
        lambda_label = QLabel("3. Passing Arguments with Lambda")
        lambda_label.setStyleSheet("font-weight: bold;")

        lambda_btn = QPushButton("Say Hello")
        lambda_btn.clicked.connect(lambda: self.on_lambda_click("Hello from Lambda"))

        main_layout.addWidget(lambda_label)
        main_layout.addWidget(lambda_btn)

        # ---------------------------
        # 4. Grouping Buttons with QButtonGroup
        # ---------------------------
        group_label = QLabel("4. Grouping Buttons with QButtonGroup")
        group_label.setStyleSheet("font-weight: bold;")

        hbox_group = QHBoxLayout()
        group = QButtonGroup(self)
        group.buttonClicked[int].connect(self.on_group_click)

        for i in range(1, 4):
            btn = QPushButton(f"Option {i}")
            group.addButton(btn, i)  # Assign ID to each button
            hbox_group.addWidget(btn)

        main_layout.addWidget(group_label)
        main_layout.addLayout(hbox_group)

        # ---------------------------
        # 5. Styling Buttons with CSS
        # ---------------------------
        style_label = QLabel("5. Styling Buttons with CSS")
        style_label.setStyleSheet("font-weight: bold;")

        style_btn = QPushButton("Styled Button")
        style_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-weight: bold;
                padding: 8px 16px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        main_layout.addWidget(style_label)
        main_layout.addWidget(style_btn)

        # ---------------------------
        # 6. Enabling/Disabling Buttons Dynamically
        # ---------------------------
        enable_label = QLabel("6. Enable/Disable Buttons Dynamically")
        enable_label.setStyleSheet("font-weight: bold;")

        enable_btn = QPushButton("Disable Me")
        enable_btn.clicked.connect(lambda: enable_btn.setDisabled(True))

        main_layout.addWidget(enable_label)
        main_layout.addWidget(enable_btn)

        # ---------------------------
        # 7. Icon Button
        # ---------------------------
        icon_label = QLabel("7. Button with Icon")
        icon_label.setStyleSheet("font-weight: bold;")

        icon_btn = QPushButton("With Icon")
        icon_btn.setIcon(QIcon.fromTheme("folder"))  # Uses system icon theme if available
        icon_btn.clicked.connect(lambda: print("Icon button clicked"))

        main_layout.addWidget(icon_label)
        main_layout.addWidget(icon_btn)

        # ---------------------------
        # Final Setup
        # ---------------------------
        self.setLayout(main_layout)

    # ---------------------------
    # Slots (Event Handlers)
    # ---------------------------
    def on_basic_click(self):
        print("Basic button clicked!")

    def on_toggle(self, checked):
        print(f"Toggle button is now {'ON' if checked else 'OFF'}")

    def on_lambda_click(self, message):
        print(message)

    def on_group_click(self, id):
        print(f"Button with ID {id} clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = ButtonDemo()
    demo.show()
    sys.exit(app.exec_())