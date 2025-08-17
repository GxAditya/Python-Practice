import random

lowest = 1
highest = 100

answer = random.randint(lowest, highest)
guesses = 0
is_running = True

print("Welcome to the Number Guessing Game!")
print(f"Select a number between {lowest} and {highest}")

while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit() and int(guess) >= lowest and int(guess) <= highest:
        guess = int(guess)
        guesses += 1
        if guess < answer:
            print("Too low")
        elif guess > answer:
            print("Too high")
        else:
            print(f"Congratulations! You guessed the number in {guesses} attempts!")
            is_running = False
    else:
        print("Please enter a valid number")
        continue