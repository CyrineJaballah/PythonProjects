import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Take a guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try guessing a higher number.")
        else:
            print("Too high! Try guessing a lower number.")

        if attempts >= 5:
            print("You have reached the maximum number of attempts.")
            print(f"The secret number was: {secret_number}")
            break

number_guessing_game()
