# Program to demonstrate the use of membership operators in Python
# Membership operators are used to test if a value is found in a sequence (string, list, tuple, set, dictionary)

def main():
    # 1. Using 'in' operator
    print("1. Using 'in' operator:")
    
    # Check if a character exists in a string
    text = "Hello, World!"
    print(f"'H' in '{text}':", 'H' in text)  # True
    print(f"'z' in '{text}':", 'z' in text)  # False
    
    # Check if an element exists in a list
    fruits = ['apple', 'banana', 'cherry']
    print(f"'banana' in {fruits}:", 'banana' in fruits)  # True
    print(f"'orange' in {fruits}:", 'orange' in fruits)  # False
    
    # 2. Using 'not in' operator
    print("\n2. Using 'not in' operator:")
    
    # Check if a character does not exist in a string
    print(f"'z' not in '{text}':", 'z' not in text)  # True
    
    # Check if an element does not exist in a list
    print(f"'orange' not in {fruits}:", 'orange' not in fruits)  # True
    
    # 3. Using membership with other data types
    print("\n3. Using membership with other data types:")
    
    # With tuples
    numbers = (1, 2, 3, 4, 5)
    print(f"3 in {numbers}:", 3 in numbers)  # True
    
    # With sets
    vowels = {'a', 'e', 'i', 'o', 'u'}
    print(f"'a' in {vowels}:", 'a' in vowels)  # True
    
    # With dictionaries (checks keys by default)
    person = {'name': 'John', 'age': 30}
    print(f"'name' in {person}:", 'name' in person)  # True
    print(f"'John' in {person}:", 'John' in person)   # False (checks keys, not values)
    print(f"'John' in {person}.values():", 'John' in person.values())  # True (checks values)

if __name__ == "__main__":
    main()
