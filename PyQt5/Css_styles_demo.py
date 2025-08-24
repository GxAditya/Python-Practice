"""
PyQt5 CSS (QSS) Styling - Detailed Guide with Examples
------------------------------------------------------
This script demonstrates:
    1. Applying styles to individual widgets
    2. Styling QPushButton, QLabel, QLineEdit, QCheckBox, QRadioButton
    3. Using pseudo-states (:hover, :pressed, :checked, :focus)
    4. Styling containers (QWidget, QFrame)
    5. Applying global styles
    6. Using IDs (#id) and classes (.class) for targeted styling

Run:
    pip install PyQt5
    python pyqt5_css_styles_demo.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QCheckBox, QRadioButton, QFrame
)
from PyQt5.QtCore import Qt


class CSSDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 CSS (QSS) Styling - Detailed Demo")
        self.setGeometry(200, 200, 500, 600)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # ---------------------------
        # 1. QLabel Styling
        # ---------------------------
        label = QLabel("Styled QLabel")
        label.setStyleSheet("""
            QLabel {
                color: #4CAF50;
                font-size: 16px;
                font-weight: bold;
            }
        """)
        main_layout.addWidget(label)

        # ---------------------------
        # 2. QPushButton Styling with States
        # ---------------------------
        btn = QPushButton("Hover & Press Me")
        btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 8px 16px;
                border-radius: 6px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
            QPushButton:pressed {
                background-color: #0D47A1;
            }
        """)
        main_layout.addWidget(btn)

        # ---------------------------
        # 3. QLineEdit Styling with Focus
        # ---------------------------
        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Focus on me...")
        line_edit.setStyleSheet("""
            QLineEdit {
                border: 2px solid gray;
                border-radius: 4px;
                padding: 4px;
            }
            QLineEdit:focus {
                border: 2px solid #4CAF50;
                background-color: #E8F5E9;
            }
        """)
        main_layout.addWidget(line_edit)

        # ---------------------------
        # 4. QCheckBox & QRadioButton Styling
        # ---------------------------
        checkbox = QCheckBox("Styled Checkbox")
        checkbox.setStyleSheet("""
            QCheckBox {
                spacing: 8px;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
            }
            QCheckBox::indicator:checked {
                background-color: #4CAF50;
                border-radius: 3px;
            }
        """)

        radio = QRadioButton("Styled RadioButton")
        radio.setStyleSheet("""
            QRadioButton {
                spacing: 8px;
                font-weight: bold;
            }
            QRadioButton::indicator {
                width: 18px;
                height: 18px;
            }
            QRadioButton::indicator:checked {
                background-color: #2196F3;
                border-radius: 9px;
            }
        """)

        main_layout.addWidget(checkbox)
        main_layout.addWidget(radio)

        # ---------------------------
        # 5. Styling a QFrame Container
        # ---------------------------
        frame = QFrame()
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setObjectName("myFrame")  # Assign ID for targeted styling
        frame.setStyleSheet("""
            QFrame#myFrame {
                background-color: #F5F5F5;
                border: 2px solid #BDBDBD;
                border-radius: 8px;
                padding: 10px;
            }
        """)
        frame_layout = QVBoxLayout()
        frame_layout.addWidget(QLabel("Inside a styled QFrame"))
        frame.setLayout(frame_layout)
        main_layout.addWidget(frame)

        # ---------------------------
        # 6. Global Styles for the App
        # ---------------------------
        # You can set styles for all widgets at once:
        self.setStyleSheet("""
            QWidget {
                font-family: Arial;
            }
        """)

        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CSSDemo()
    demo.show()
    sys.exit(app.exec_())