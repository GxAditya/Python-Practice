import sys
from PyQt5.QtWidgets import QApplication , QWidget , QVBoxLayout , QLabel , QPushButton , QHBoxLayout
from PyQt5.QtCore import Qt , QTimer , QTime
from PyQt5.QtGui import QFont , QFontDatabase

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stopwatch")
        self.setGeometry(100, 100, 300, 200)
        self.setStyleSheet("background-color: #000000")
        self.time = QTime(0, 0, 0 , 0)
        self.time_label = QLabel("00:00:00:00" , self)
        self.time_label.setAlignment(Qt.AlignCenter)
        QFontDatabase.addApplicationFont("mini-apps/alarm clock.ttf")
        self.time_label.setFont(QFont("alarm clock" , 20))
        self.time_label.setStyleSheet("color: #26ff00")


        self.start_button = QPushButton("Start" , self)
        self.start_button.setStyleSheet("background-color: #26ff00; border-radius: 20px;")
        self.start_button.clicked.connect(self.start_stopwatch)

        self.stop_button = QPushButton("Stop" , self)
        self.stop_button.setStyleSheet("background-color: #26ff00; border-radius: 20px;")
        self.stop_button.clicked.connect(self.stop_stopwatch)

        self.reset_button = QPushButton("Reset" , self)
        self.reset_button.setStyleSheet("background-color: #26ff00; border-radius: 20px;")
        self.reset_button.clicked.connect(self.reset_stopwatch)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.time_label)
        self.layout.addWidget(self.start_button)
        self.layout.addWidget(self.stop_button)
        self.layout.addWidget(self.reset_button)
        self.setLayout(self.layout)

    def start_stopwatch(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(10)

    def update_time(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.time.toString("hh:mm:ss:zzz"))

    def stop_stopwatch(self):
        self.timer.stop()

    def reset_stopwatch(self):
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText("00:00:00:00")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())