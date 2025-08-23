def display_cart(items, prices, quantities):
    print("\n{:<20} {:<10} {:<10} {:<10}".format('Item', 'Price', 'Quantity', 'Total'))
    print("-" * 50)
    for item, price, qty in zip(items, prices, quantities):
        print("{:<20} ${:<9.2f} {:<10} ${:<10.2f}".format(item, price, qty, price * qty))

# Initialize empty lists to store items, prices, and quantities
item_list = []
price_list = []
quantity_list = []

def main():
    print("=== Shopping Cart ===")
    print("Enter item details (or 'c' to checkout)")
    print("-" * 30)
    
    while True:
        # Get item name
        item = input("\nItem name (or 'c' to checkout): ").strip()
        if item.lower() == 'c':
            break
            
        # Get quantity
        while True:
            try:
                quantity = input("Quantity: ").strip()
                if quantity.lower() == 'c':
                    return display_checkout(item_list, price_list, quantity_list)
                quantity = int(quantity)
                if quantity > 0:
                    break
                print("Please enter a positive number")
            except ValueError:
                print("Please enter a valid number")
        
        # Get price
        while True:
            try:
                price = input("Price per item: $").strip()
                if price.lower() == 'c':
                    return display_checkout(item_list, price_list, quantity_list)
                price = float(price)
                if price >= 0:
                    break
                print("Price cannot be negative")
            except ValueError:
                print("Please enter a valid price")
        
        # Add item to cart
        item_list.append(item)
        price_list.append(price)
        quantity_list.append(quantity)
        
        # Show current cart
        display_cart(item_list, price_list, quantity_list)
    
    display_checkout(item_list, price_list, quantity_list)

def display_checkout(items, prices, quantities):
    if not items:
        print("\nYour cart is empty!")
        return
    
    print("\n" + "="*50)
    print("YOUR SHOPPING CART")
    print("="*50)
    
    display_cart(items, prices, quantities)
    
    # Calculate and display total
    total = sum(price * qty for price, qty in zip(prices, quantities))
    print("-" * 50)
    print("{:>40} ${:.2f}".format("TOTAL:", total))
    print("="*50 + "\n")
    print("Thank you for shopping with us!")

if __name__ == "__main__":
    main()