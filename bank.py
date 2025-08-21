import time

# ASCII Art for the bank logo
BANK_LOGO = """
  ____              _    _             _    
 |  _ \            | |  (_)           | |   
 | |_) | __ _ _ __ | | ___ _ __   __ _| | __
 |  _ < / _` | '_ \| |/ / | '_ \ / _` | |/ /
 | |_) | (_| | | | |   <| | | | | (_| |   < 
 |____/ \__,_|_| |_|_|\_\_|_| |_|\__,_|_|\_\
                                             
"""

def show_balance(balance):
    print("\n" + "="*50)
    print(f"💰 Your current balance is: ${balance:.2f}")
    print("="*50)

def deposit(balance):
    print("\n" + "💰 DEPOSIT ".ljust(50, '='))
    try:
        amount = float(input("\nEnter amount to deposit: $"))
        if amount <= 0:
            print("\n❌ Error: Deposit amount must be greater than zero")
        else:
            balance += amount
            print(f"\n✅ Successfully deposited ${amount:.2f}")
            print(f"💵 New balance: ${balance:.2f}")
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
    return balance

def withdraw(balance):
    print("\n" + "💵 WITHDRAW ".ljust(50, '='))
    try:
        amount = float(input("\nEnter amount to withdraw: $"))
        if amount <= 0:
            print("\n❌ Error: Withdrawal amount must be greater than zero")
        elif amount > balance:
            print("\n❌ Error: Insufficient funds")
        else:
            balance -= amount
            print(f"\n✅ Successfully withdrew ${amount:.2f}")
            print(f"💵 New balance: ${balance:.2f}")
    except ValueError:
        print("\n❌ Invalid input. Please enter a valid number.")
    return balance

def print_menu():
    print("\n" + " MENU ".center(50, '='))
    print("1. Show Balance")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Exit")
    print("="*50)

def main():
    balance = 0.0
    
    # Clear screen and show welcome message
    print("\n" * 5)
    print(BANK_LOGO)
    print("Welcome to Python Banking App!".center(50))
    print("="*50)
    time.sleep(1)
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            print("\n" + " THANK YOU ".center(50, '='))
            print("\nThank you for using Python Banking App! 👋")
            print("Have a great day! 😊")
            print("="*50 + "\n")
            break
        else:
            print("\n❌ Invalid choice. Please enter a number between 1 and 4.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
