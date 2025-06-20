import random

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user = input("\nChoose Rock, Paper, or Scissors: ").lower()
        if user not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")
            continue

        computer = random.choice(['rock', 'paper', 'scissors'])
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")

        if user == computer:
            print("It's a tie!")
        elif (user == 'rock' and computer == 'scissors') or \
             (user == 'paper' and computer == 'rock') or \
             (user == 'scissors' and computer == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")

        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing. Goodbye!")
            break

play_game()
