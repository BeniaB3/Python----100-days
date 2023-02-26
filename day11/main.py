import random
import art
from art import logo


def create_deck():
    """Creates a deck of cards"""
    deck = {
        "Ace": 11,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Jack": 10,
        "Queen": 10,
        "King": 10,
    }
    return deck


def draw_card(deck):
    """Draws a card from the deck"""
    card = random.choice(list(deck.keys()))
    value = deck[card]
    return card, value


def calculate_score(cards):
    """Calculates the score of the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return "Blackjack"
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Compares the user's score to the computer's score"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, your opponent has a Blackjack"
    elif user_score == 0:
        return "Win! You have a Blackjack"
    elif user_score == "Blackjack":
        return "Wow! You have a Blackjack"
    elif computer_score == "Blackjack":
        return "Lose, your opponent has a Blackjack"
    elif user_score > 21:
        return "Over than 21. You lose!"
    elif computer_score > 21:
        return "Your opponent went over. You win!"
    elif user_score > computer_score:
        return "Your score is higher than your opponent. You win!"
    else:
        return "You lose"


def play_game():
    """Plays a game of Blackjack"""
    deck = create_deck()
    user_cards = []
    user_score = 0

    computer_cards = []
    computer_score = 0

    is_game_over = False

    for _ in range(2):
        card, value = draw_card(deck)
        user_cards.append(value)
        print(f"You drew a {card}")
        card, value = draw_card(deck)
        computer_cards.append(value)

    while not is_game_over:
        print(logo)
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {list(deck.keys())[0]}, current score: {computer_cards[0]} + ?")

        if user_score == "Blackjack" or computer_score == "Blackjack" or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                card, value = draw_card(deck)
                user_cards.append(value)
                print(f"You drew a {card}")
            else:
                is_game_over = True

    while computer_score != "Blackjack" and computer_score < 17:
        card, value = draw_card(deck)
        computer_cards.append(value)
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))
    print(deck)

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        play_game()


play_game()
