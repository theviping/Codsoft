import random
def game():
    user_score = 0
    computer_score = 0
    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nRock, Paper, Scissors Game")
        print("Enter your choice:")
        user_choice = input().lower()
        if user_choice not in choices:
            print("Invalid choice. Please choose either rock, paper or scissors.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

        print(f"Score: User - {user_score}, Computer - {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

game()