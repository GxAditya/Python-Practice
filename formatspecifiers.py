# format specifiers : {value : flags} format a value based on what flags are inserted

price1 = 3.14528
price2 = 4.258654
price3 = 50.332631

print(f"Price1 is {price1:.2f}") # formats the price to 2 decimal places
print(f"Price2 is {price2:.3f}") # formats the price to 3 decimal places

# More Python Format Specifiers Examples

# String formatting
name = "Alex"
# {:s} - Format as string
print("Name: {:s}".format(name))

# Integer formatting
age = 27
# {:d} - Decimal integer
# {:b} - Binary format
# {:o} - Octal format
# {:x} / {:X} - Hexadecimal format (lowercase/uppercase)
print("Age (decimal): {:d}".format(age))
print("Age (binary): {:b}".format(age))
print("Age (octal): {:o}".format(age))
print("Age (hex lowercase): {:x}".format(age))
print("Age (hex uppercase): {:X}".format(age))

# Float formatting
pi = 3.14159
# {:f} - Fixed-point format
# {:.2f} - Two decimal places
# {:e} / {:E} - Scientific notation
# {:g} / {:G} - General format
print("Pi (fixed-point): {:f}".format(pi))
print("Pi (2 decimals): {:.2f}".format(pi))
print("Pi (scientific): {:e}".format(pi))
print("Pi (general): {:g}".format(pi))

# Alignment and padding
# {:<10} - Left-align within 10 characters
# {:>10} - Right-align
# {:^10} - Center-align
# {:0>5d} - Zero-pad on the left (width 5)
print("Left-align: {:<10}".format(name))
print("Right-align: {:>10}".format(name))
print("Center-align: {:^10}".format(name))
print("Zero-padded age: {:0>5d}".format(age))
