# Program to demonstrate list comprehensions in Python
# List comprehensions provide a concise way to create lists

def main():
    # 1. Basic list comprehension
    # Create a list of squares from 0 to 9
    squares = [x**2 for x in range(10)]
    print(f"1. Squares: {squares}")
    
    # 2. List comprehension with condition
    # Get only even numbers from 0 to 9
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"2. Even numbers: {evens}")
    
    # 3. List comprehension with if-else
    # Replace even numbers with 'even' and odd with 'odd'
    even_odd = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
    print(f"3. Even/Odd mapping: {even_odd}")
    
    # 4. Nested list comprehensions
    # Create a 3x3 matrix
    matrix = [[i + j for j in range(3)] for i in range(0, 9, 3)]
    print("4. 3x3 Matrix:")
    for row in matrix:
        print(f"   {row}")
    
    # 5. List comprehension with strings
    sentence = "List comprehensions are awesome!"
    # Get all vowels from the sentence
    vowels = [char for char in sentence.lower() if char in 'aeiou']
    print(f"5. Vowels in sentence: {vowels}")
    
    # 6. List comprehension with dictionary
    names = ['Alice', 'Bob', 'Charlie', 'David']
    # Create a dictionary with name lengths
    name_lengths = {name: len(name) for name in names}
    print(f"6. Name lengths: {name_lengths}")
    
    # 7. Flattening a 2D list
    matrix_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix_2d for num in row]
    print(f"7. Flattened matrix: {flattened}")
    
    # 8. List comprehension with function
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    # Get prime numbers up to 30
    primes = [x for x in range(2, 31) if is_prime(x)]
    print(f"8. Prime numbers up to 30: {primes}")
    
    # 9. List comprehension with multiple lists
    colors = ['red', 'green', 'blue']
    fruits = ['apple', 'banana', 'cherry']
    # Create all possible color-fruit combinations
    combinations = [(color, fruit) for color in colors for fruit in fruits]
    print("9. Color-Fruit combinations:")
    for i, combo in enumerate(combinations, 1):
        print(f"   {i}. {combo[0].title()} {combo[1]}")
    
    # 10. List comprehension with set (removing duplicates)
    numbers = [1, 2, 2, 3, 4, 4, 5]
    unique_squares = {x**2 for x in numbers}
    print(f"10. Unique squares: {sorted(unique_squares)}")

if __name__ == "__main__":
    main()
