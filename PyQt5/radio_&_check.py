"""
PyQt5 Checkboxes & Radio Buttons - Detailed Guide with Examples
---------------------------------------------------------------
This script demonstrates:
    1. Basic QCheckBox usage
    2. Tri-state checkboxes
    3. Connecting signals to slots
    4. Basic QRadioButton usage
    5. Grouping radio buttons with QButtonGroup
    6. Enabling/disabling widgets based on selection
    7. Styling checkboxes and radio buttons

Run:
    pip install PyQt5
    python pyqt5_check_radio_demo.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QCheckBox, QRadioButton, QButtonGroup, QPushButton
)
from PyQt5.QtCore import Qt


class CheckRadioDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Checkboxes & Radio Buttons - Detailed Demo")
        self.setGeometry(200, 200, 500, 500)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # ---------------------------
        # 1. Basic QCheckBox
        # ---------------------------
        cb_label = QLabel("1. Basic QCheckBox")
        cb_label.setStyleSheet("font-weight: bold;")

        self.basic_cb = QCheckBox("I agree to the terms and conditions")
        self.basic_cb.stateChanged.connect(self.on_basic_checkbox)

        main_layout.addWidget(cb_label)
        main_layout.addWidget(self.basic_cb)

        # ---------------------------
        # 2. Tri-state QCheckBox
        # ---------------------------
        tri_label = QLabel("2. Tri-state QCheckBox")
        tri_label.setStyleSheet("font-weight: bold;")

        self.tri_cb = QCheckBox("Tri-state Example")
        self.tri_cb.setTristate(True)  # Allows partial check state
        self.tri_cb.stateChanged.connect(self.on_tri_checkbox)

        main_layout.addWidget(tri_label)
        main_layout.addWidget(self.tri_cb)

        # ---------------------------
        # 3. QRadioButton Basics
        # ---------------------------
        rb_label = QLabel("3. Basic QRadioButton")
        rb_label.setStyleSheet("font-weight: bold;")

        self.rb1 = QRadioButton("Option A")
        self.rb2 = QRadioButton("Option B")
        self.rb3 = QRadioButton("Option C")

        # Group them so only one can be selected
        self.radio_group = QButtonGroup(self)
        self.radio_group.addButton(self.rb1, 1)
        self.radio_group.addButton(self.rb2, 2)
        self.radio_group.addButton(self.rb3, 3)
        self.radio_group.buttonClicked[int].connect(self.on_radio_selected)

        main_layout.addWidget(rb_label)
        main_layout.addWidget(self.rb1)
        main_layout.addWidget(self.rb2)
        main_layout.addWidget(self.rb3)

        # ---------------------------
        # 4. Enable/Disable based on selection
        # ---------------------------
        enable_label = QLabel("4. Enable/Disable Button based on Checkbox")
        enable_label.setStyleSheet("font-weight: bold;")

        self.enable_cb = QCheckBox("Enable Submit Button")
        self.enable_cb.stateChanged.connect(self.toggle_submit)

        self.submit_btn = QPushButton("Submit")
        self.submit_btn.setEnabled(False)

        main_layout.addWidget(enable_label)
        main_layout.addWidget(self.enable_cb)
        main_layout.addWidget(self.submit_btn)

        # ---------------------------
        # 5. Styling Checkboxes & Radio Buttons
        # ---------------------------
        style_label = QLabel("5. Styling Checkboxes & Radio Buttons")
        style_label.setStyleSheet("font-weight: bold;")

        styled_cb = QCheckBox("Styled Checkbox")
        styled_cb.setStyleSheet("""
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

        styled_rb = QRadioButton("Styled Radio")
        styled_rb.setStyleSheet("""
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

        main_layout.addWidget(style_label)
        main_layout.addWidget(styled_cb)
        main_layout.addWidget(styled_rb)

        self.setLayout(main_layout)

    # ---------------------------
    # Slots (Event Handlers)
    # ---------------------------
    def on_basic_checkbox(self, state):
        if state == Qt.Checked:
            print("Basic checkbox: Checked")
        else:
            print("Basic checkbox: Unchecked")

    def on_tri_checkbox(self, state):
        if state == Qt.PartiallyChecked:
            print("Tri-state checkbox: Partially Checked")
        elif state == Qt.Checked:
            print("Tri-state checkbox: Checked")
        else:
            print("Tri-state checkbox: Unchecked")

    def on_radio_selected(self, id):
        print(f"Radio button with ID {id} selected")

    def toggle_submit(self, state):
        self.submit_btn.setEnabled(state == Qt.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = CheckRadioDemo()
    demo.show()
    sys.exit(app.exec_())