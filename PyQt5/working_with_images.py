from cProfile import label
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtGui import QIcon , QFont , QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        label = QLabel(self)
        label.setGeometry(0,0 , self.height() , self.width())

        pixmap = QPixmap("PyQt5/image.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()