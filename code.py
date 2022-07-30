import random

user = input("Enter a choice (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer = random.choice(possible_actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")

if user == computer:
    print(f"Both players selected {user}. It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("Paper covers rock! You lose.")
    else:
        print("Rock smashes scissors! You win!")
elif user == "paper":
    if computer == "rock":
        print("Scissors cuts paper! You lose.")
    else:
        print("Paper covers rock! You win!")
elif user == "scissors":
    if computer == "paper":
        print("Rock smashes scissors! You lose.")
    else:
        print("Scissors cuts paper! You win!")
