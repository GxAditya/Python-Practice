"""
write_csv_x_mode.py

Demonstrates writing CSV data to a file using 'x' mode.
File path: file-handling/data.csv

'x' mode:
---------
- Creates a new file for writing.
- Raises FileExistsError if the file already exists.
"""

import csv
import os

# Define the file path
file_path = os.path.join("file-handling", "data.csv")

# Sample CSV data
csv_data = [
    ["Name", "Age", "City"],
    ["Alice", 28, "New York"],
    ["Bob", 34, "London"],
    ["Charlie", 25, "Sydney"]
]

# Ensure the directory exists
os.makedirs(os.path.dirname(file_path), exist_ok=True)

try:
    # Open file in 'x' mode to create it exclusively
    with open(file_path, mode="x", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(csv_data)
    print(f"✅ File created and data written successfully at: {file_path}")

except FileExistsError:
    print(f"❌ File already exists at: {file_path}. No data was overwritten.")

except OSError as e:
    print(f"❌ OS error occurred: {e}")