import random

def play_game():
    print("Let's play Rock, Paper, Scissors!")
    print("Choose one: Rock, Paper, or Scissors")
    
    choices = ["rock", "paper", "scissors"]
    
    while True:
        user_choice = input("Your choice: ").lower()
        
        if user_choice not in choices:
            print("Invalid input. Please choose again.")
            continue
        
        computer_choice = random.choice(choices)
        
        print(f"You chose {user_choice.capitalize()}")
        print(f"The computer chose {computer_choice.capitalize()}")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            print("You win!")
        else:
            print("Computer wins!")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        
        if play_again != "yes":
            break

play_game()
