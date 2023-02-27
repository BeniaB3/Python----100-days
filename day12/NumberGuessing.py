import random
import art

print(art.logo)


def game(lvl_of_game):
    lives = 10
    number_to_guess = random.randint(1, 100)
    if lvl_of_game == "hard":
        lives = 5
    while lives > 0:
        print(f"You have {lives} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == number_to_guess:
            print(f"You got it! The answer was {number_to_guess}")
            return
        elif guess > number_to_guess:
            print("Too high.")
            lives -= 1
        elif guess < number_to_guess:
            print("Too low.")
            lives -= 1
    print("You've run out of guesses, you lose.")


print("Welcome to the number guessing game!")
play = True
while play:
    lvl = input("Choose a difficulty. Type 'easy' or 'hard': ")
    game(lvl)
    play = input("Do you still want to play? Type 'y' or 'n': ")
    if play == "n":
        play = False
        print("Goodbye!")