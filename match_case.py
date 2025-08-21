# Program to demonstrate match-case statements in Python (Python 3.10+)
# Match-case is a structural pattern matching feature

def process_http_status(code):
    """Process HTTP status codes using match-case"""
    match code:
        case 200:
            return "OK - Request successful"
        case 301 | 302:  # Multiple values in one case
            return f"{code} - Redirect"
        case 400:
            return "Bad Request - Client error"
        case 401 | 403:  # Multiple values with same action
            return f"{code} - Unauthorized/Forbidden"
        case 404:
            return "Not Found - Resource doesn't exist"
        case 500:
            return "Internal Server Error"
        case _:  # Default case (like 'else' in if-elif-else)
            return f"{code} - Unknown status code"

def process_data(data):
    """Process different types of data using pattern matching"""
    match data:
        case []:  # Empty list
            return "Received an empty list"
        case [x]:  # List with one element
            return f"Single element list: {x}"
        case [x, y]:  # List with exactly two elements
            return f"Two elements: {x} and {y}"
        case [x, y, *rest]:  # List with at least two elements
            return f"First: {x}, Second: {y}, Rest: {rest}"
        case _:
            return "Not a list or empty"

def process_person(person):
    """Process person data with pattern matching"""
    match person:
        case {"name": name, "age": age} if age >= 18:  # Dictionary with name and age
            return f"{name} is an adult (Age: {age})"
        case {"name": name, "age": age}:
            return f"{name} is a minor (Age: {age})"
        case {"name": name}:
            return f"Name provided: {name}, age unknown"
        case _:
            return "Invalid person data"

def process_shape(shape):
    """Process different shapes with pattern matching"""
    match shape:
        case ("circle", radius):
            return f"Circle with radius {radius}"
        case ("rectangle", width, height):
            return f"Rectangle {width}x{height}"
        case ("square", side):
            return f"Square with side {side}"
        case _:
            return "Unknown shape"

def main():
    # 1. HTTP Status Code Example
    print("1. HTTP Status Codes:")
    status_codes = [200, 301, 404, 500, 999]
    for code in status_codes:
        print(f"   {code}: {process_http_status(code)}")
    
    # 2. List Pattern Matching
    print("\n2. List Processing:")
    lists = [[], [1], [1, 2], [1, 2, 3, 4, 5], "hello"]
    for lst in lists:
        print(f"   {lst} -> {process_data(lst)}")
    
    # 3. Person Data Processing
    print("\n3. Person Data:")
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 15},
        {"name": "Charlie"},
        {}
    ]
    for person in people:
        print(f"   {person} -> {process_person(person)}")
    
    # 4. Shape Processing
    print("\n4. Shape Processing:")
    shapes = [
        ("circle", 5),
        ("rectangle", 4, 6),
        ("square", 3),
        ("triangle", 1, 2, 3)
    ]
    for shape in shapes:
        print(f"   {shape} -> {process_shape(shape)}")
    
    # 5. Advanced: Matching with classes (Python 3.10+)
    print("\n5. Class Pattern Matching:")
    from dataclasses import dataclass
    
    @dataclass
    class Point:
        x: int
        y: int
    
    def process_point(point):
        match point:
            case Point(x=0, y=0):
                return "Origin"
            case Point(x=0, y=y):
                return f"On Y-axis at y={y}"
            case Point(x=x, y=0):
                return f"On X-axis at x={x}"
            case Point(x=x, y=y):
                return f"Point at ({x}, {y})"
    
    points = [Point(0, 0), Point(0, 5), Point(3, 0), Point(2, 3)]
    for point in points:
        print(f"   {point} -> {process_point(point)}")

if __name__ == "__main__":
    main()
