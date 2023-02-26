import random

your_choice = input("Choose rock, paper or scissors: ")
computer_choice = random.choice(["rock", "paper", "scissors"])

your_choice = your_choice.lower()

print("Your choice:")

if your_choice == "rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif your_choice == "paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif your_choice == "scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)
print("Computer choice:")

if computer_choice == "rock":
    print("""
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    """)
elif computer_choice == "paper":
    print("""
         _______
    ---'    ____)____
               ______)
              _______)
             _______)
    ---.__________)
    """)
elif computer_choice == "scissors":
    print("""
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    """)

if your_choice == computer_choice:
    print("Draw!")
elif your_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    else:
        print("You lose!")
elif your_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    else:
        print("You lose!")
elif your_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    else:
        print("You lose!")
