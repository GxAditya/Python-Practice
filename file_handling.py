"""
file_utility_toolkit.py

A complete file management utility with:
- Create / Write / Append
- Read (full, line-by-line, partial)
- Check existence
- Rename / Delete
- List files in a directory
- Copy / Move files
- Create directories
- Handle binary files (images, PDFs)
- Robust exception handling
"""

import os
import shutil

# ---------------------------
# File Creation & Writing
# ---------------------------

def create_and_write_file(filename, content):
    """Creates a file and writes text content."""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
        print(f"✅ File '{filename}' created and written successfully.")
    except OSError as e:
        print(f"❌ Error creating/writing file: {e}")

def append_to_file(filename, content):
    """Appends text to an existing file."""
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write("\n" + content)
        print(f"✅ Content appended to '{filename}'.")
    except FileNotFoundError:
        print(f"❌ Cannot append — file '{filename}' not found.")
    except OSError as e:
        print(f"❌ Error appending to file: {e}")

# ---------------------------
# File Reading
# ---------------------------

def read_file_full(filename):
    """Reads the entire file content."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"📖 Full content of '{filename}':\n{file.read()}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except OSError as e:
        print(f"❌ Error reading file: {e}")

def read_file_line_by_line(filename):
    """Reads a file line by line."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"📖 Reading '{filename}' line by line:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except OSError as e:
        print(f"❌ Error reading file: {e}")

def read_file_partial(filename, num_chars):
    """Reads a specific number of characters from a file."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(f"📖 First {num_chars} characters of '{filename}':\n{file.read(num_chars)}")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except OSError as e:
        print(f"❌ Error reading file: {e}")

# ---------------------------
# File Checks & Management
# ---------------------------

def check_file_exists(filename):
    """Checks if a file exists."""
    exists = os.path.exists(filename)
    print(f"🔍 File '{filename}' exists: {exists}")
    return exists

def rename_file(old_name, new_name):
    """Renames a file."""
    try:
        os.rename(old_name, new_name)
        print(f"✅ File renamed from '{old_name}' to '{new_name}'.")
    except FileNotFoundError:
        print(f"❌ File '{old_name}' not found.")
    except OSError as e:
        print(f"❌ Error renaming file: {e}")

def delete_file(filename):
    """Deletes a file."""
    try:
        os.remove(filename)
        print(f"🗑️ File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except OSError as e:
        print(f"❌ Error deleting file: {e}")

# ---------------------------
# Directory Operations
# ---------------------------

def list_files_in_directory(directory):
    """Lists all files in a directory."""
    try:
        files = os.listdir(directory)
        print(f"📂 Files in '{directory}': {files}")
    except FileNotFoundError:
        print(f"❌ Directory '{directory}' not found.")
    except OSError as e:
        print(f"❌ Error listing directory: {e}")

def create_directory(directory):
    """Creates a directory if it doesn't exist."""
    try:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Directory '{directory}' created or already exists.")
    except OSError as e:
        print(f"❌ Error creating directory: {e}")

# ---------------------------
# File Copy & Move
# ---------------------------

def copy_file(src, dest):
    """Copies a file to a new location."""
    try:
        shutil.copy(src, dest)
        print(f"✅ File copied from '{src}' to '{dest}'.")
    except FileNotFoundError:
        print(f"❌ Source file '{src}' not found.")
    except OSError as e:
        print(f"❌ Error copying file: {e}")

def move_file(src, dest):
    """Moves a file to a new location."""
    try:
        shutil.move(src, dest)
        print(f"✅ File moved from '{src}' to '{dest}'.")
    except FileNotFoundError:
        print(f"❌ Source file '{src}' not found.")
    except OSError as e:
        print(f"❌ Error moving file: {e}")

# ---------------------------
# Binary File Handling
# ---------------------------

def copy_binary_file(src, dest):
    """Copies binary files like images or PDFs."""
    try:
        with open(src, "rb") as fsrc:
            with open(dest, "wb") as fdest:
                fdest.write(fsrc.read())
        print(f"✅ Binary file copied from '{src}' to '{dest}'.")
    except FileNotFoundError:
        print(f"❌ Binary file '{src}' not found.")
    except OSError as e:
        print(f"❌ Error copying binary file: {e}")

# ---------------------------
# Demo Usage
# ---------------------------

if __name__ == "__main__":
    # Create and write
    create_and_write_file("sample.txt", "Hello, World!")

    # Append
    append_to_file("sample.txt", "This is an appended line.")

    # Read
    read_file_full("sample.txt")
    read_file_line_by_line("sample.txt")
    read_file_partial("sample.txt", 5)

    # Check existence
    check_file_exists("sample.txt")

    # Directory operations
    create_directory("backup")
    list_files_in_directory(".")

    # Copy & Move
    copy_file("sample.txt", "backup/sample_copy.txt")
    move_file("backup/sample_copy.txt", "backup/sample_moved.txt")

    # Rename
    rename_file("sample.txt", "renamed_sample.txt")

    # Binary file copy example (if you have an image)
    # copy_binary_file("image.jpg", "backup/image_copy.jpg")

    # Delete
    delete_file("renamed_sample.txt")
    delete_file("backup/sample_moved.txt")