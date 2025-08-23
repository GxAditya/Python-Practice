import os

file_path = "test.txt"
"""
Detecting Files and Directories
"""

# Check if file exists
if os.path.exists(file_path):
    print("File exists")

    # Check if it's a file or directory
    if os.path.isfile(file_path):
        print("It is a file")
    elif os.path.isdir(file_path):
        print("It is a directory")
else:
    print("File does not exist")

# Writing to Files

with open(file_path, "w") as file:
    file.write("Hello, World!")

# Appending to Files

with open(file_path, "a") as file:
    file.write("\nAppended text")

# Reading from Files

with open(file_path, "r") as file:
    content = file.read()
    print(content)

# Deleting Files

os.remove(file_path)

# Renaming Files

os.rename("test.txt", "new_test.txt")

# Copying Files

os.copy("new_test.txt", "copy_new_test.txt")

# Moving Files

os.rename("copy_new_test.txt", "moved_new_test.txt")

# Listing Files in a Directory

files = os.listdir(".")
print(files)

# Creating Directories

os.mkdir("new_directory")

# Removing Directories

os.rmdir("new_directory")
