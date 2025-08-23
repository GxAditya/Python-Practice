import random

def get_dice_face(value):
    """Returns ASCII art for a dice face with the given value"""
    faces = {
        1: [
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ],
        2: [
            "┌───────┐",
            "│ ●     │",
            "│       │",
            "│     ● │",
            "└───────┘"
        ],
        3: [
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ],
        4: [
            "┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"
        ],
        5: [
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
        ],
        6: [
            "┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"
        ]
    }
    return faces.get(value, ["Invalid dice value"] * 5)

def display_dice_rolls(dice_faces):
    """Display multiple dice faces side by side"""
    for i in range(5):  # Each dice face has 5 lines
        line = "  ".join(face[i] for face in dice_faces)
        print(line)

def main():
    lowest = 1
    highest = 6
    
    while True:
        try:
            num_rolls = int(input("How many times do you want to roll the dice? "))
            if num_rolls <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    total = 0
    all_rolls = []
    
    for _ in range(num_rolls):
        roll = random.randint(lowest, highest)
        total += roll
        all_rolls.append(roll)
    
    print("\nDice Rolled:")
    display_dice_rolls([get_dice_face(roll) for roll in all_rolls])
    print(f"\nTotal sum of all rolls: {total}")
    
    # Show the total as a sum of dice faces (if possible)
    if total <= 6 * 5:  # Limit to reasonable number of dice to display
        print("\nTotal shown as dice:")
        # Calculate how to represent the total with dice (maximum 5 dice)
        remaining = total
        total_dice = []
        while remaining > 0 and len(total_dice) < 5:  # Max 5 dice to display
            dice_value = min(6, remaining)
            total_dice.append(get_dice_face(dice_value))
            remaining -= dice_value
        
        # Display the dice representing the total
        for i in range(5):  # Each dice face has 5 lines
            line = "  ".join(dice[i] for dice in total_dice)
            print(line)
    
    print(f"\nTotal: {total}")
    
    play_again = input("\nRoll again? (yes(y)/no(n)): ").lower()
    if play_again in ["yes", "y"]:
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    print("=== Dice Roller ===")
    print("Roll the dice and see the total displayed as dice!\n")
    main()
