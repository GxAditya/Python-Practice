import sys
import requests
import json
from datetime import datetime
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QPushButton, QLineEdit, 
                            QFrame, QMessageBox, QGridLayout)
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor

class WeatherWorker(QThread):
    weather_data = pyqtSignal(dict)
    error_occurred = pyqtSignal(str)
    
    def __init__(self, city, api_key):
        super().__init__()
        self.city = city
        self.api_key = api_key
    
    def run(self):
        try:
            # Current weather API endpoint
            current_url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
            
            # Make API request
            response = requests.get(current_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                self.weather_data.emit(data)
            elif response.status_code == 404:
                self.error_occurred.emit("City not found. Please check the city name.")
            elif response.status_code == 401:
                self.error_occurred.emit("Invalid API key. Please check your OpenWeather API key.")
            else:
                self.error_occurred.emit(f"Error fetching weather data: {response.status_code}")
                
        except requests.exceptions.Timeout:
            self.error_occurred.emit("Request timed out. Please check your internet connection.")
        except requests.exceptions.ConnectionError:
            self.error_occurred.emit("Connection error. Please check your internet connection.")
        except Exception as e:
            self.error_occurred.emit(f"An unexpected error occurred: {str(e)}")

class WeatherApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.api_key = "87894d7f218afea1e4e27e3d1e1e1ed4"  # Replace with your actual API key
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("Weather App")
        self.setGeometry(100, 100, 500, 700)
        self.setMinimumSize(400, 600)
        
        # Set up the main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)
        layout.setSpacing(20)
        layout.setContentsMargins(20, 20, 20, 20)
        
        # Set dark theme
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #2C3E50, stop:1 #34495E);
            }
            QWidget {
                background-color: transparent;
                color: white;
            }
            QLineEdit {
                background-color: rgba(255, 255, 255, 0.1);
                border: 2px solid #3498DB;
                border-radius: 15px;
                padding: 10px 15px;
                font-size: 14px;
                color: white;
            }
            QLineEdit:focus {
                border-color: #E74C3C;
                background-color: rgba(255, 255, 255, 0.15);
            }
            QPushButton {
                background-color: #3498DB;
                border: none;
                border-radius: 15px;
                padding: 12px 25px;
                font-size: 14px;
                font-weight: bold;
                color: white;
            }
            QPushButton:hover {
                background-color: #2980B9;
            }
            QPushButton:pressed {
                background-color: #21618C;
            }
            QLabel {
                color: white;
            }
            QFrame {
                background-color: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                padding: 15px;
            }
        """)
        
        # Title
        title = QLabel("🌤️ Weather App")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Arial", 24, QFont.Bold))
        title.setStyleSheet("color: #E8F6F3; margin-bottom: 10px;")
        layout.addWidget(title)
        
        # Search section
        search_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name...")
        self.city_input.returnPressed.connect(self.get_weather)
        
        self.search_btn = QPushButton("🔍 Search")
        self.search_btn.clicked.connect(self.get_weather)
        
        search_layout.addWidget(self.city_input)
        search_layout.addWidget(self.search_btn)
        layout.addLayout(search_layout)
        
        # Weather info frame
        self.weather_frame = QFrame()
        self.weather_layout = QVBoxLayout(self.weather_frame)
        self.weather_layout.setAlignment(Qt.AlignCenter)
        
        # City and date
        self.city_label = QLabel("Enter a city to see weather")
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.city_label.setStyleSheet("color: #AED6F1;")
        
        self.date_label = QLabel("")
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont("Arial", 12))
        self.date_label.setStyleSheet("color: #D5DBDB;")
        
        # Weather icon and temperature
        self.weather_icon = QLabel("🌡️")
        self.weather_icon.setAlignment(Qt.AlignCenter)
        self.weather_icon.setFont(QFont("Arial", 48))
        
        self.temp_label = QLabel("")
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setFont(QFont("Arial", 36, QFont.Bold))
        self.temp_label.setStyleSheet("color: #F8C471;")
        
        self.desc_label = QLabel("")
        self.desc_label.setAlignment(Qt.AlignCenter)
        self.desc_label.setFont(QFont("Arial", 14))
        self.desc_label.setStyleSheet("color: #AED6F1;")
        
        # Weather details grid
        details_frame = QFrame()
        details_frame.setStyleSheet("background-color: rgba(255, 255, 255, 0.05); border-radius: 10px;")
        self.details_layout = QGridLayout(details_frame)
        
        # Create detail labels
        self.feels_like_label = QLabel("")
        self.humidity_label = QLabel("")
        self.pressure_label = QLabel("")
        self.wind_label = QLabel("")
        self.visibility_label = QLabel("")
        self.uv_index_label = QLabel("")
        
        # Style detail labels
        detail_labels = [self.feels_like_label, self.humidity_label, self.pressure_label, 
                        self.wind_label, self.visibility_label, self.uv_index_label]
        
        for label in detail_labels:
            label.setFont(QFont("Arial", 11))
            label.setStyleSheet("color: #D5DBDB; padding: 5px;")
        
        # Add widgets to weather layout
        self.weather_layout.addWidget(self.city_label)
        self.weather_layout.addWidget(self.date_label)
        self.weather_layout.addWidget(self.weather_icon)
        self.weather_layout.addWidget(self.temp_label)
        self.weather_layout.addWidget(self.desc_label)
        self.weather_layout.addWidget(details_frame)
        
        layout.addWidget(self.weather_frame)
        
        # Add some spacing
        layout.addStretch()
        
        # Update time every minute
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_time)
        self.timer.start(60000)  # Update every minute
        
        # Initial time update
        self.update_time()
        
    def update_time(self):
        current_time = datetime.now().strftime("%A, %B %d, %Y - %I:%M %p")
        if hasattr(self, 'date_label'):
            self.date_label.setText(current_time)
    
    def get_weather(self):
        city = self.city_input.text().strip()
        
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name!")
            return
            
        if self.api_key == "YOUR_API_KEY_HERE":
            QMessageBox.critical(self, "API Key Error", 
                               "Please set your OpenWeatherMap API key in the code!\n\n" +
                               "Get your free API key from: https://openweathermap.org/api")
            return
        
        # Disable search button during API call
        self.search_btn.setEnabled(False)
        self.search_btn.setText("Loading...")
        
        # Create and start worker thread
        self.worker = WeatherWorker(city, self.api_key)
        self.worker.weather_data.connect(self.update_weather_display)
        self.worker.error_occurred.connect(self.handle_error)
        self.worker.finished.connect(self.on_request_finished)
        self.worker.start()
    
    def update_weather_display(self, data):
        try:
            # Extract data
            city_name = data['name']
            country = data['sys']['country']
            temp = round(data['main']['temp'])
            feels_like = round(data['main']['feels_like'])
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            description = data['weather'][0]['description'].title()
            wind_speed = data['wind']['speed']
            visibility = data.get('visibility', 0) // 1000  # Convert to km
            
            # Get weather icon
            weather_id = data['weather'][0]['id']
            icon = self.get_weather_icon(weather_id)
            
            # Update UI
            self.city_label.setText(f"{city_name}, {country}")
            self.temp_label.setText(f"{temp}°C")
            self.desc_label.setText(description)
            self.weather_icon.setText(icon)
            
            # Update details grid
            self.details_layout.addWidget(QLabel("🌡️ Feels like:"), 0, 0)
            self.feels_like_label.setText(f"{feels_like}°C")
            self.details_layout.addWidget(self.feels_like_label, 0, 1)
            
            self.details_layout.addWidget(QLabel("💧 Humidity:"), 1, 0)
            self.humidity_label.setText(f"{humidity}%")
            self.details_layout.addWidget(self.humidity_label, 1, 1)
            
            self.details_layout.addWidget(QLabel("🌪️ Pressure:"), 2, 0)
            self.pressure_label.setText(f"{pressure} hPa")
            self.details_layout.addWidget(self.pressure_label, 2, 1)
            
            self.details_layout.addWidget(QLabel("💨 Wind Speed:"), 0, 2)
            self.wind_label.setText(f"{wind_speed} m/s")
            self.details_layout.addWidget(self.wind_label, 0, 2)
            
            self.details_layout.addWidget(QLabel("👁️ Visibility:"), 1, 2)
            self.visibility_label.setText(f"{visibility} km")
            self.details_layout.addWidget(self.visibility_label, 1, 3)
            
        except KeyError as e:
            self.handle_error(f"Error parsing weather data: Missing {e}")
    
    def get_weather_icon(self, weather_id):
        """Return appropriate emoji based on weather condition ID"""
        if 200 <= weather_id <= 232:
            return "⛈️"  # Thunderstorm
        elif 300 <= weather_id <= 321:
            return "🌦️"  # Drizzle
        elif 500 <= weather_id <= 531:
            return "🌧️"  # Rain
        elif 600 <= weather_id <= 622:
            return "❄️"  # Snow
        elif 701 <= weather_id <= 781:
            return "🌫️"  # Atmosphere (fog, haze, etc.)
        elif weather_id == 800:
            return "☀️"  # Clear sky
        elif 801 <= weather_id <= 804:
            return "⛅"  # Clouds
        else:
            return "🌤️"  # Default
    
    def handle_error(self, error_message):
        QMessageBox.critical(self, "Error", error_message)
        
    def on_request_finished(self):
        self.search_btn.setEnabled(True)
        self.search_btn.setText("🔍 Search")

def main():
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName("Weather App")
    app.setOrganizationName("PyQt Weather")
    
    window = WeatherApp()
    window.show()
    
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()