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


def who_has_more(person1, person2):
    if person1["follower_count"] > person2['follower_count']:
        return person1
    else:
        return person2

