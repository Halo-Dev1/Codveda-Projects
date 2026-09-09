import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7  # You can adjust this number

    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed the number in {attempt} attempts.")
            return

    print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}.")

# Run the game
number_guessing_game()
