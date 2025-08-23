"""
read_multiple_file_types.py

Demonstrates reading data from:
1. JSON files
2. CSV files
3. TXT files

Includes:
- Exception handling
- Clean, reusable functions
"""

import json
import csv
import os

# ---------------------------
# JSON Reading
# ---------------------------

def read_json_file(filepath):
    """Reads and prints data from a JSON file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            data = json.load(file)
        print(f"📄 JSON Data from '{filepath}':")
        print(data)
        return data
    except FileNotFoundError:
        print(f"❌ JSON file '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"❌ Error decoding JSON: {e}")
    except OSError as e:
        print(f"❌ OS error reading JSON file: {e}")

# ---------------------------
# CSV Reading
# ---------------------------

def read_csv_file(filepath):
    """Reads and prints data from a CSV file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            print(f"📄 CSV Data from '{filepath}':")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print(f"❌ CSV file '{filepath}' not found.")
    except OSError as e:
        print(f"❌ OS error reading CSV file: {e}")

# ---------------------------
# TXT Reading
# ---------------------------

def read_txt_file(filepath):
    """Reads and prints data from a TXT file."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            print(f"📄 TXT Data from '{filepath}':")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"❌ TXT file '{filepath}' not found.")
    except OSError as e:
        print(f"❌ OS error reading TXT file: {e}")

# ---------------------------
# Example Usage
# ---------------------------

if __name__ == "__main__":
    # Example file paths (adjust as needed)
    json_path = os.path.join("file-handling", "data.json")
    csv_path = os.path.join("file-handling", "data.csv")
    txt_path = os.path.join("file-handling", "notes.txt")

    # Read each file type
    read_json_file(json_path)
    print("-" * 50)
    read_csv_file(csv_path)
    print("-" * 50)
    read_txt_file(txt_path)