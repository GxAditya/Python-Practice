import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIcon , QFont
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(100, 100, 300, 200)
        self.setWindowIcon(QIcon("PyQt5/image.jpg"))
        self.layout = QVBoxLayout()
        self.label = QLabel("Hello, PyQt5!")
        self.label.setFont(QFont("Arial", 16)) # Font
        self.label.setStyleSheet("color: red") # text color
        self.label.setAlignment(Qt.AlignCenter) # text alignment
        self.button = QPushButton("Click Me")  # Button
        self.button.clicked.connect(self.on_click) # Button click event
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def on_click(self):
        self.label.setText("Button Clicked!")   # Button click event


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()        