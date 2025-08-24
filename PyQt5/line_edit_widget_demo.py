"""
PyQt5 QLineEdit - Detailed Guide with Examples
----------------------------------------------
This script demonstrates:
    1. Basic QLineEdit usage
    2. Placeholder text
    3. Echo modes (Normal, Password, NoEcho)
    4. Input masks
    5. Validators (Int, Double, Regex)
    6. Signals: textChanged, returnPressed
    7. Read-only fields
    8. Styling QLineEdit

Run:
    pip install PyQt5
    python pyqt5_lineedit_demo.py
"""

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit
)
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class LineEditDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 QLineEdit - Detailed Demo")
        self.setGeometry(200, 200, 500, 500)

        self.init_ui()

    def init_ui(self):
        main_layout = QVBoxLayout()

        # ---------------------------
        # 1. Basic QLineEdit
        # ---------------------------
        basic_label = QLabel("1. Basic QLineEdit")
        basic_label.setStyleSheet("font-weight: bold;")

        self.basic_le = QLineEdit()
        self.basic_le.setText("Hello, PyQt5!")  # Set initial text
        self.basic_le.textChanged.connect(self.on_text_changed)

        main_layout.addWidget(basic_label)
        main_layout.addWidget(self.basic_le)

        # ---------------------------
        # 2. Placeholder Text
        # ---------------------------
        placeholder_label = QLabel("2. Placeholder Text")
        placeholder_label.setStyleSheet("font-weight: bold;")

        placeholder_le = QLineEdit()
        placeholder_le.setPlaceholderText("Enter your name here...")

        main_layout.addWidget(placeholder_label)
        main_layout.addWidget(placeholder_le)

        # ---------------------------
        # 3. Echo Modes
        # ---------------------------
        echo_label = QLabel("3. Echo Modes")
        echo_label.setStyleSheet("font-weight: bold;")

        normal_le = QLineEdit()
        normal_le.setPlaceholderText("Normal mode (visible text)")

        password_le = QLineEdit()
        password_le.setPlaceholderText("Password mode")
        password_le.setEchoMode(QLineEdit.Password)

        noecho_le = QLineEdit()
        noecho_le.setPlaceholderText("NoEcho mode (nothing visible)")
        noecho_le.setEchoMode(QLineEdit.NoEcho)

        main_layout.addWidget(echo_label)
        main_layout.addWidget(normal_le)
        main_layout.addWidget(password_le)
        main_layout.addWidget(noecho_le)

        # ---------------------------
        # 4. Input Masks
        # ---------------------------
        mask_label = QLabel("4. Input Masks")
        mask_label.setStyleSheet("font-weight: bold;")

        phone_le = QLineEdit()
        phone_le.setPlaceholderText("Phone: +99-9999-999999")
        phone_le.setInputMask("+99-9999-999999;_")

        date_le = QLineEdit()
        date_le.setPlaceholderText("Date: DD/MM/YYYY")
        date_le.setInputMask("00/00/0000;_")

        main_layout.addWidget(mask_label)
        main_layout.addWidget(phone_le)
        main_layout.addWidget(date_le)

        # ---------------------------
        # 5. Validators
        # ---------------------------
        validator_label = QLabel("5. Validators")
        validator_label.setStyleSheet("font-weight: bold;")

        int_le = QLineEdit()
        int_le.setPlaceholderText("Integer between 1 and 100")
        int_le.setValidator(QIntValidator(1, 100, self))

        double_le = QLineEdit()
        double_le.setPlaceholderText("Double between 0.0 and 99.99")
        double_le.setValidator(QDoubleValidator(0.0, 99.99, 2, self))

        regex_le = QLineEdit()
        regex_le.setPlaceholderText("Only letters allowed")
        regex_validator = QRegExpValidator(QRegExp("[A-Za-z]+"), self)
        regex_le.setValidator(regex_validator)

        main_layout.addWidget(validator_label)
        main_layout.addWidget(int_le)
        main_layout.addWidget(double_le)
        main_layout.addWidget(regex_le)

        # ---------------------------
        # 6. Signals
        # ---------------------------
        signal_label = QLabel("6. Signals: textChanged & returnPressed")
        signal_label.setStyleSheet("font-weight: bold;")

        signal_le = QLineEdit()
        signal_le.setPlaceholderText("Type and press Enter...")
        signal_le.textChanged.connect(lambda text: print(f"Text changed: {text}"))
        signal_le.returnPressed.connect(lambda: print("Return pressed!"))

        main_layout.addWidget(signal_label)
        main_layout.addWidget(signal_le)

        # ---------------------------
        # 7. Read-only Field
        # ---------------------------
        readonly_label = QLabel("7. Read-only QLineEdit")
        readonly_label.setStyleSheet("font-weight: bold;")

        readonly_le = QLineEdit("You can't edit this")
        readonly_le.setReadOnly(True)

        main_layout.addWidget(readonly_label)
        main_layout.addWidget(readonly_le)

        # ---------------------------
        # 8. Styling QLineEdit
        # ---------------------------
        style_label = QLabel("8. Styling QLineEdit")
        style_label.setStyleSheet("font-weight: bold;")

        styled_le = QLineEdit()
        styled_le.setPlaceholderText("Styled input")
        styled_le.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4CAF50;
                border-radius: 6px;
                padding: 4px;
                font-weight: bold;
            }
            QLineEdit:focus {
                border-color: #2196F3;
                background-color: #E3F2FD;
            }
        """)

        main_layout.addWidget(style_label)
        main_layout.addWidget(styled_le)

        self.setLayout(main_layout)

    # ---------------------------
    # Slots (Event Handlers)
    # ---------------------------
    def on_text_changed(self, text):
        print(f"Basic QLineEdit text changed: {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = LineEditDemo()
    demo.show()
    sys.exit(app.exec_())