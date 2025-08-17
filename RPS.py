import random

options = ("rock", "paper", "scissors")

computer = random.choice(options)





while True:
    player = input("Enter your choice (rock/paper/scissors): ").lower()

    while player not in options:
        player = input("Invalid choice. Please try again: ").lower()

    print(f"Computer chose: {computer}")
    print(f"Player chose: {player}")
    
    if player == computer:
        print("Tie!")
    elif player == "rock" and computer == "scissors":
        print("Player wins!")
    elif player == "paper" and computer == "rock":
        print("Player wins!")
    elif player == "scissors" and computer == "paper":
        print("Player wins!")
    else:
        print("Computer wins!")
    
    play_again = input("Play again? (yes(y)/no(n)): ").lower()
    if play_again != "yes" or "y":
        break


