import json
import os 

file_path = "file-handling/data.json"

Bio = {
    "name": "Aditya",
    "age": 20,
    "city": "Bhilai",
    "education": "B.tech",
    "college" :"SSTC"
}


try:
    with open(file_path, "x") as file:
        json.dump(Bio, file, indent=4)
except FileExistsError:
    print("File already exists")