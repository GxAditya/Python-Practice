import random
import time
import os
from colorama import init, Fore, Style

#pip install colorama

# Initialize colorama
init(autoreset=True)

# Slot machine symbols with their values
SYMBOLS = {
    '🍒': 2,
    '🍋': 3,
    '🍊': 4,
    '🍇': 5,
    '🔔': 6,
    '7️⃣': 10,
    '💎': 15
}

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(balance):
    """Print the game header with current balance."""
    print(Fore.CYAN + "=" * 50)
    print(Fore.YELLOW + "🎰" + Fore.CYAN + " PYTHON SLOT MACHINE " + Fore.YELLOW + "🎰")
    print(Fore.CYAN + "=" * 50)
    print(f"{Fore.GREEN}Balance: ${balance}{Style.RESET_ALL}")
    print()

def spin_reels():
    """Generate a random spin result."""
    return [random.choice(list(SYMBOLS.keys())) for _ in range(3)]

def calculate_win(spin, bet):
    """Calculate winnings based on spin result."""
    # Check for three of a kind
    if len(set(spin)) == 1:
        return bet * SYMBOLS[spin[0]] * 2
    
    # Check for two of a kind
    for symbol in set(spin):
        if spin.count(symbol) == 2:
            return bet * SYMBOLS[symbol]
    
    return 0

def print_spin_animation():
    """Show a spinning animation."""
    for _ in range(5):
        for frame in "|/-\\":
            print(f"\rSpinning... {frame}", end="", flush=True)
            time.sleep(0.1)
    print("\r" + " " * 20 + "\r", end="")

def play_slot_machine():
    """Main game loop."""
    balance = 100  # Starting balance
    
    while True:
        clear_screen()
        print_header(balance)
        
        if balance <= 0:
            print(Fore.RED + "Game Over! You're out of money!")
            break
            
        try:
            bet = int(input("Enter your bet (0 to quit): $"))
            
            if bet == 0:
                print(f"\nThanks for playing! You're leaving with ${balance}!")
                break
                
            if bet < 1:
                print(Fore.RED + "Minimum bet is $1!")
                time.sleep(1)
                continue
                
            if bet > balance:
                print(Fore.RED + "You don't have enough money for that bet!")
                time.sleep(1)
                continue
                
            # Deduct bet from balance
            balance -= bet
            
            # Show spinning animation
            print()
            print_spin_animation()
            
            # Get spin result
            spin = spin_reels()
            
            # Display the result
            print(f"\n{Fore.CYAN}>> {Fore.YELLOW}{' | '.join(spin)} {Fore.CYAN}<<\n")
            
            # Calculate winnings
            winnings = calculate_win(spin, bet)
            
            if winnings > 0:
                balance += winnings
                print(Fore.GREEN + f"🎉 You won ${winnings}! 🎉")
            else:
                print(Fore.RED + "No win this time. Try again!")
            
            # Pause before next spin
            input(f"\n{Fore.WHITE}Press Enter to spin again...")
            
        except ValueError:
            print(Fore.RED + "Please enter a valid number!")
            time.sleep(1)
        except KeyboardInterrupt:
            print(f"\n\nThanks for playing! You're leaving with ${balance}!")
            break

if __name__ == "__main__":
    try:
        play_slot_machine()
    except KeyboardInterrupt:
        print("\nGame stopped by user. Thanks for playing!")