"""
api_requests_demo.py

This script demonstrates working with APIs in Python using the 'requests' library.

What is an API?
---------------
- API = Application Programming Interface.
- A set of rules that allows software to communicate with other software.
- Web APIs allow you to send HTTP requests (GET, POST, PUT, DELETE) to a server and receive data back.

We will cover:
1. Making a GET request
2. Sending query parameters
3. Making a POST request with JSON data
4. Handling JSON responses
5. Error handling for network/API issues
"""

import requests

# ---------------------------
# 1. Basic GET Request
# ---------------------------

def get_example():
    """Makes a GET request to a public API."""
    url = "https://jsonplaceholder.typicode.com/posts/1"  # Fake API for testing
    try:
        response = requests.get(url, timeout=5)  # timeout in seconds
        response.raise_for_status()  # Raises HTTPError for bad responses (4xx, 5xx)
        data = response.json()  # Convert JSON response to Python dict
        print("✅ GET Request Successful:")
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"❌ GET Request Failed: {e}")

# ---------------------------
# 2. GET Request with Query Parameters
# ---------------------------

def get_with_params():
    """Makes a GET request with query parameters."""
    url = "https://jsonplaceholder.typicode.com/comments"
    params = {"postId": 1}  # Filter comments for postId=1
    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("✅ GET with Params Successful:")
        for comment in data[:3]:  # Show first 3 comments
            print(comment)
    except requests.exceptions.RequestException as e:
        print(f"❌ GET with Params Failed: {e}")

# ---------------------------
# 3. POST Request with JSON Data
# ---------------------------

def post_example():
    """Makes a POST request to send JSON data."""
    url = "https://jsonplaceholder.typicode.com/posts"
    payload = {
        "title": "My New Post",
        "body": "This is the content of the post.",
        "userId": 1
    }
    try:
        response = requests.post(url, json=payload, timeout=5)
        response.raise_for_status()
        data = response.json()
        print("✅ POST Request Successful:")
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"❌ POST Request Failed: {e}")

# ---------------------------
# 4. Handling Non-JSON Responses
# ---------------------------

def get_text_response():
    """Handles APIs that return plain text instead of JSON."""
    url = "https://httpbin.org/ip"  # Returns JSON, but we can also get text
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        print("✅ Text Response:")
        print(response.text)  # Raw text
    except requests.exceptions.RequestException as e:
        print(f"❌ Text Response Failed: {e}")

# ---------------------------
# 5. Main Execution
# ---------------------------

if __name__ == "__main__":
    print("=== API GET Example ===")
    get_example()
    print("\n=== API GET with Params ===")
    get_with_params()
    print("\n=== API POST Example ===")
    post_example()
    print("\n=== API Text Response Example ===")
    get_text_response()