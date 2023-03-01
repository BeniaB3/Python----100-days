import art
import game_data
import random

print(art.logo)


def random_person():
    return random.choice(game_data.data)


def compare(person1, person2):
    while person1 == person2:
        person2 = random_person()
    return person2


def random_to_game():
    person1 = random_person()
    person2 = random_person()
    person2 = compare(person1, person2)
    return person1, person2


def who_has_more_followers(person1, person2):
    if person1['follower_count'] > person2['follower_count']:
        return person1
    else:
        return person2


def print_person(person1, person2):
    print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}")
    print(art.vs)
    print(f"Against B: {person2['name']}, a {person2['description']}, from {person2['country']}")
    return input("Who has more followers? Type 'A' or 'B': ")


def check_answer(person1, person2, answer):
    if answer == 'A':
        if person1['follower_count'] > person2['follower_count']:
            return True
        else:
            return False
    elif answer == 'B':
        if person2['follower_count'] > person1['follower_count']:
            return True
        else:
            return False


def game():
    score = 0
    do_you_want_to_play = input("Do you want to play a game of Higher Lower? Type 'y' or 'n': ")
    person1 = random_person()
    while do_you_want_to_play == 'y':
        person2 = random_person()
        person2 = compare(person1, person2)
        answer = print_person(person1, person2)
        if check_answer(person1, person2, answer):
            score += 1
            print(f"You're right! Current score: {score}")
            person1 = who_has_more_followers(person1, person2)
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            do_you_want_to_play = input("Do you want to play a game of Higher Lower? Type 'y' or 'n': ")
            if do_you_want_to_play == 'y':
                person1 = random_person()
            score = 0
    print("Goodbye!")


game()
