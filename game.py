import random


def game():
    print("Welcome to rock, paper, scissors game!".upper())
    print("Type 'exit' to quit.")

    while True:
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        user_choice = input("Enter rock, paper or scissors: ").lower()
        if user_choice == "exit":
            print("Bye bye!")
            break
        if user_choice not in options:
            print("Please Enter rock, paper or scissors")
            continue

        if user_choice == computer_choice:
            print("User:", user_choice)
            print("Computer:", computer_choice)
            print("Tie!")
        elif user_choice == "rock":
            if computer_choice == "paper":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You lose!")
            if computer_choice == "scissors":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You win!")
        elif user_choice == "scissors":
            if computer_choice == "rock":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You lose!")
            if computer_choice == "paper":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You win!")
        elif user_choice == "paper":
            if computer_choice == "scissors":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You lose!")
            if computer_choice == "rock":
                print("User:", user_choice)
                print("Computer:", computer_choice)
                print("You win!")


if __name__ == "__main__":
    game()
