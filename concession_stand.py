menu = {
    "nachos": 12,
    "burger": 15,
    "fries": 5,
    "soda": 3,  
    "pizza":6,
    "chicken wings": 10,
    "chocolate cake": 7,
    "ice cream": 4,
    "pasta": 18,
    "tacos": 10,
    "salad": 12,
    "chicken sandwich": 13,
    "onion rings": 11,
    "brownie": 8,
    "cola": 7,
    }

cart = []
total = 0


print("Welcome to the Concession Stand!")
print("-------------Menu----------------")
for item, price in menu.items():
    print(f"{item:<20}: ${price:.2f}")

while True:
    item = input("\n What would you like to order(press q to quit):").lower()
    if item == "q":
        break
    elif menu.get(item) is not None:
        cart.append(item)

for item in cart :
    total += menu.get(item)  
    print(item , end=" ")    

print()
print("---------------------------------")
print(f"Total: ${total:.2f}")     