# Import required modules
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont , QFontDatabase

class DigitalClock(QWidget):
    """
    A digital clock application using PyQt5.
    Displays the current time in HH:MM:SS AM/PM format with a green digital display.
    """
    def __init__(self):
        """Initialize the DigitalClock window and set up the UI."""
        super().__init__()
        self.setWindowTitle("Digital Clock")
        self.setGeometry(200, 200, 300, 100)  # x, y, width, height

        self.init_ui()  # Initialize the user interface

    def init_ui(self):
        """Set up the user interface components and timer."""
        main_layout = QVBoxLayout()

        # Create and configure the time display label
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)  # Center align the text
        QFontDatabase.addApplicationFont("mini-apps/alarm clock.ttf")
        self.label.setFont(QFont("alarm clock" , 20))  # Set font style and size
        self.label.setStyleSheet("color: #26ff00")  # Set text color to green
        self.setStyleSheet("background-color: #000000")  # Set background to black

        # Add the label to the layout
        main_layout.addWidget(self.label)
        self.setLayout(main_layout)

        # Set up a timer to update the clock every second (1000ms)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)  # Update every 1000ms (1 second)

    def update_time(self):
        """Update the displayed time with the current time."""
        current_time = QTime.currentTime()  # Get current time
        time_text = current_time.toString("hh:mm:ss AP")  # Format as HH:MM:SS AM/PM
        self.label.setText(time_text)  # Update the label with current time


if __name__ == "__main__":
    # Create and run the application
    app = QApplication(sys.argv)  # Create the application object
    clock = DigitalClock()  # Create an instance of our DigitalClock
    clock.show()  # Display the clock window
    sys.exit(app.exec_())  # Start the application event loop