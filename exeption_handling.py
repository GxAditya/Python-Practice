"""
exception_handling_demo.py

This script demonstrates Python's exception handling using:
- try / except
- multiple except blocks
- else
- finally
- raising exceptions
- custom exceptions

Exception Handling:
-------------------
- Exceptions are runtime errors that disrupt the normal flow of a program.
- Python uses try/except blocks to catch and handle exceptions gracefully.
"""

# ---------------------------
# 1. Basic try/except
# ---------------------------

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
        result = None
    return result

print(divide(10, 2))  # Output: 5.0
print(divide(10, 0))  # Output: Error message + None


# ---------------------------
# 2. Multiple except blocks
# ---------------------------

def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print("Error: Value must be a number.")
    except TypeError:
        print("Error: Unsupported type for conversion.")

print(safe_convert("42"))   # Output: 42
print(safe_convert("abc"))  # Output: Error message
print(safe_convert(None))   # Output: Error message


# ---------------------------
# 3. Using else and finally
# ---------------------------

def read_file(filename):
    try:
        file = open(filename, "r")
    except FileNotFoundError:
        print("Error: File not found.")
    else:
        # Runs only if no exception occurred
        content = file.read()
        print("File content:", content)
        file.close()
    finally:
        # Always runs, whether exception occurred or not
        print("Finished attempting to read file.")

read_file("example.txt")  # Try with an existing and non-existing file


# ---------------------------
# 4. Raising exceptions
# ---------------------------

def withdraw(balance, amount):
    if amount > balance:
        raise ValueError("Insufficient funds.")
    return balance - amount

try:
    print(withdraw(100, 50))  # Works fine
    print(withdraw(100, 150)) # Will raise ValueError
except ValueError as e:
    print(f"Transaction failed: {e}")


# ---------------------------
# 5. Custom exceptions
# ---------------------------

class NegativeNumberError(Exception):
    """Custom exception for negative numbers."""
    pass

def square_root(num):
    if num < 0:
        raise NegativeNumberError("Cannot take square root of a negative number.")
    return num ** 0.5

try:
    print(square_root(9))   # Output: 3.0
    print(square_root(-4))  # Will raise NegativeNumberError
except NegativeNumberError as e:
    print(f"Custom Error: {e}")


"""
Key Takeaways:
--------------
1. try/except:
   - Wrap risky code in try.
   - Handle specific exceptions in except blocks.

2. Multiple except blocks:
   - Catch different exception types separately.

3. else:
   - Runs only if no exception occurs.

4. finally:
   - Always runs, useful for cleanup (closing files, releasing resources).

5. raise:
   - Manually trigger exceptions when invalid conditions occur.

6. Custom exceptions:
   - Create by subclassing Exception.
   - Useful for domain-specific error handling.
"""


"""
Real life example:
"""

"""
safe_file_manager.py

A small utility for safe file operations with:
- Read
- Write / Append
- Backup before overwrite
- Error logging

Demonstrates real-world exception handling patterns.
"""

import os
import shutil
from datetime import datetime

ERROR_LOG = "error.log"

def log_error(message):
    """Logs error messages to a separate error log file with timestamps."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(ERROR_LOG, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
    except OSError as e:
        print(f"❌ Failed to write to error log: {e}")


def backup_file(filepath):
    """Creates a backup of the file before overwriting."""
    if os.path.exists(filepath):
        backup_name = f"{filepath}.bak_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        try:
            shutil.copy(filepath, backup_name)
            print(f"📦 Backup created: {backup_name}")
        except OSError as e:
            print(f"❌ Failed to create backup: {e}")
            log_error(f"Backup failed for {filepath}: {e}")


def read_file(filepath):
    """Reads and prints file content with exception handling."""
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            print(f"📖 Reading file: {filepath}")
            print(file.read())
    except FileNotFoundError:
        msg = f"File not found: {filepath}"
        print(f"❌ {msg}")
        log_error(msg)
    except PermissionError:
        msg = f"Permission denied: {filepath}"
        print(f"❌ {msg}")
        log_error(msg)
    except OSError as e:
        msg = f"OS error while reading {filepath}: {e}"
        print(f"❌ {msg}")
        log_error(msg)
    finally:
        print("📌 Read operation complete.\n")


def write_file(filepath, content, overwrite=False):
    """
    Writes content to a file.
    If overwrite=False, appends instead.
    Creates a backup before overwriting.
    """
    try:
        if overwrite:
            backup_file(filepath)
            mode = "w"
        else:
            mode = "a"

        with open(filepath, mode, encoding="utf-8") as file:
            file.write(content + "\n")
        print(f"✅ Successfully {'overwritten' if overwrite else 'appended to'} {filepath}")
    except PermissionError:
        msg = f"Permission denied while writing to {filepath}"
        print(f"❌ {msg}")
        log_error(msg)
    except OSError as e:
        msg = f"OS error while writing to {filepath}: {e}"
        print(f"❌ {msg}")
        log_error(msg)
    finally:
        print("📌 Write operation complete.\n")


if __name__ == "__main__":
    test_file = "data.txt"

    # Try reading before file exists
    read_file(test_file)

    # Append some data
    write_file(test_file, "First log entry")
    write_file(test_file, "Second log entry")

    # Read after writing
    read_file(test_file)

    # Overwrite with backup
    write_file(test_file, "Overwritten content", overwrite=True)

    # Read again
    read_file(test_file)

    # Simulate permission error (Unix only)
    if os.name != "nt":
        os.chmod(test_file, 0o000)  # Remove all permissions
        read_file(test_file)
        write_file(test_file, "This will fail")
        os.chmod(test_file, 0o644)  # Restore permissions