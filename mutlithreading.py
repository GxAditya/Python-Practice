"""
multithreading_demo.py

This script demonstrates multithreading in Python with detailed explanations.

What is Multithreading?
-----------------------
- Multithreading allows multiple threads (smaller units of a process) to run concurrently.
- Useful for I/O-bound tasks (e.g., file reading, network requests) where threads can work while others wait.
- In Python, due to the Global Interpreter Lock (GIL), CPU-bound tasks don't get true parallel execution with threads.
  For CPU-bound tasks, multiprocessing is better.
- For I/O-bound tasks, multithreading can significantly improve performance.

We will cover:
1. Creating and starting threads
2. Passing arguments to threads
3. Waiting for threads with join()
4. Synchronizing threads with Lock
5. A real-world simulation example
"""

import threading
import time

# ---------------------------
# 1. Basic Thread Example
# ---------------------------

def print_numbers():
    """Function to print numbers from 1 to 5 with a delay."""
    for i in range(1, 6):
        print(f"[{threading.current_thread().name}] Number: {i}")
        time.sleep(0.5)  # Simulate work

def print_letters():
    """Function to print letters A to E with a delay."""
    for letter in ["A", "B", "C", "D", "E"]:
        print(f"[{threading.current_thread().name}] Letter: {letter}")
        time.sleep(0.5)

# Create threads
t1 = threading.Thread(target=print_numbers, name="NumberThread")
t2 = threading.Thread(target=print_letters, name="LetterThread")

print("=== Starting Basic Threads ===")
t1.start()
t2.start()

# Wait for both threads to finish
t1.join()
t2.join()
print("=== Basic Threads Finished ===\n")


# ---------------------------
# 2. Passing Arguments to Threads
# ---------------------------

def greet_user(name, delay):
    """Greets a user after a delay."""
    time.sleep(delay)
    print(f"[{threading.current_thread().name}] Hello, {name}!")

print("=== Starting Threads with Arguments ===")
users = [("Alice", 1), ("Bob", 2), ("Charlie", 1.5)]
threads = []

for name, delay in users:
    t = threading.Thread(target=greet_user, args=(name, delay), name=f"Greet-{name}")
    threads.append(t)
    t.start()

# Wait for all greeting threads
for t in threads:
    t.join()
print("=== Threads with Arguments Finished ===\n")


# ---------------------------
# 3. Synchronizing Threads with Lock
# ---------------------------

counter = 0
counter_lock = threading.Lock()

def increment_counter():
    """Increments a shared counter safely using a Lock."""
    global counter
    for _ in range(100000):
        with counter_lock:  # Lock ensures only one thread modifies counter at a time
            counter += 1

print("=== Starting Counter Increment with Lock ===")
t1 = threading.Thread(target=increment_counter)
t2 = threading.Thread(target=increment_counter)

t1.start()
t2.start()
t1.join()
t2.join()

print(f"Final Counter Value: {counter}")
print("=== Counter Increment Finished ===\n")


# ---------------------------
# 4. Real-World Simulation Example
# ---------------------------

def download_file(file_name, delay):
    """Simulates downloading a file."""
    print(f"[{threading.current_thread().name}] Starting download: {file_name}")
    time.sleep(delay)  # Simulate network delay
    print(f"[{threading.current_thread().name}] Finished download: {file_name}")

print("=== Starting File Download Simulation ===")
files = [("file1.zip", 2), ("file2.zip", 3), ("file3.zip", 1)]
download_threads = []

for file_name, delay in files:
    t = threading.Thread(target=download_file, args=(file_name, delay), name=f"Downloader-{file_name}")
    download_threads.append(t)
    t.start()

# Wait for all downloads to finish
for t in download_threads:
    t.join()

print("=== All Downloads Completed ===")