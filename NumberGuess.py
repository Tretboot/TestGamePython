# This is a python code for a simple number guessing game
# The program generates a random number between 1 and 100
# The user has to guess the number in 10 attempts
# The program gives feedback on whether the guess is too high or too low

import random

# Generate a random number
number = random.randint(1, 100)

# Initialize the number of attempts
attempts = 0

# Loop until the user guesses the number or runs out of attempts
while True:
    # Ask the user to enter a guess
    guess = int(input("Enter your guess: "))

    # Increment the number of attempts
    attempts += 1

    # Check if the guess is correct
    if guess == number:
        # Congratulate the user and break the loop
        print(f"You guessed it in {attempts} attempts!")
        break
    # Check if the guess is too high
    elif guess > number:
        # Tell the user to guess lower
        print("Too high. Guess lower.")
    # Check if the guess is too low
    else:
        # Tell the user to guess higher
        print("Too low. Guess higher.")

    # Check if the user has run out of attempts
    if attempts == 10:
        # Tell the user they lost and reveal the number
        print(f"You ran out of attempts. The number was {number}.")
        break
