from replit import clear
# HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)
print("Welcome to the secret auction program.")

players = {}
game = True
while game:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    new_player = {name: bid}
    players.update(new_player)
    more = input("Are there any other bidders? Type 'yes' or 'no'.")
    if more == "no":
        game = False
        highest_bid = 0
        winner = ""
        for player in players:
            if players[player] > highest_bid:
                highest_bid = players[player]
                winner = player
        print(f"The winner is {winner} with a bid of ${highest_bid}.")
        print("The all bids were with players:")

        for player in players:
            print(f"{player} bid ${players[player]}")

    elif more == "yes":
        clear()
