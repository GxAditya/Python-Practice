# Program to demonstrate Python's LEGB rule for variable scope resolution
# LEGB stands for: Local -> Enclosing -> Global -> Built-in

# 1. Built-in scope (B in LEGB)
# These are Python's built-in functions and variables
print("1. Built-in scope (B in LEGB):")
print(f"   Built-in functions: {dir(__builtins__)[:5]}...")  # First few built-in functions

# 2. Global scope (G in LEGB)
# Variables defined at the module level
GLOBAL_VAR = "I'm a global variable"

def test_scope():
    # 3. Enclosing scope (E in LEGB)
    # Variables in the local scope of an enclosing function
    enclosing_var = "I'm in the enclosing scope"
    
    def inner_function():
        # 4. Local scope (L in LEGB)
        # Variables defined within the current function
        local_var = "I'm a local variable"
        print("\n4. Local scope (L in LEGB):")
        print(f"   Local variable: {local_var}")
        
        # Accessing enclosing scope variable
        print("\n3. Enclosing scope (E in LEGB):")
        print(f"   Enclosing variable: {enclosing_var}")
        
        # Accessing global variable
        print("\n2. Global scope (G in LEGB):")
        print(f"   Global variable: {GLOBAL_VAR}")
        
        # Accessing built-in function
        print("\n1. Built-in scope (B in LEGB):")
        print(f"   Using built-in len(): {len('hello')}")
    
    return inner_function()

# Demonstrate variable shadowing
def demonstrate_shadowing():
    print("\n=== Variable Shadowing ===")
    x = "global x"
    
    def outer():
        x = "outer x"
        
        def inner():
            x = "inner x"
            print(f"   Inner x: {x}")
        
        inner()
        print(f"   Outer x: {x}")
    
    outer()
    print(f"   Global x: {x}")

# Demonstrate nonlocal and global keywords
def demonstrate_keywords():
    print("\n=== nonlocal and global keywords ===")
    
    # Global variable
    counter = 0
    
    def outer():
        # Enclosing variable
        outer_var = "outer"
        
        def inner():
            # Tell Python we want to modify the enclosing scope variable
            nonlocal outer_var
            outer_var = "modified outer"
            
            # Tell Python we want to modify the global variable
            global counter
            counter += 1
            
            print(f"   Inside inner: outer_var = {outer_var}, counter = {counter}")
        
        inner()
        print(f"   After inner: outer_var = {outer_var}")
    
    print(f"   Before outer: counter = {counter}")
    outer()
    print(f"   After outer: counter = {counter}")

# Demonstrate LEGB with built-in shadowing
def demonstrate_builtin_shadowing():
    print("\n=== Shadowing Built-ins ===")
    
    # Shadowing the built-in 'list' function
    list = [1, 2, 3]  # This shadows the built-in list() function
    print(f"   Shadowed list: {list}")
    
    # To use the built-in list function now, we can use __builtins__.list
    new_list = __builtins__.list((4, 5, 6))
    print(f"   Using __builtins__.list: {new_list}")
    
    # Better practice: don't shadow built-in names
    numbers = [1, 2, 3]  # Use a different name instead

# Run all demonstrations
def main():
    print("=== LEGB Rule in Action ===")
    test_scope()
    demonstrate_shadowing()
    demonstrate_keywords()
    demonstrate_builtin_shadowing()
    
    # Show how to check scopes
    print("\n=== Checking Scopes ===")
    print("   Local variables:", locals().keys())
    print("   Global variables:", [var for var in globals() if not var.startswith('__')])

if __name__ == "__main__":
    main()
