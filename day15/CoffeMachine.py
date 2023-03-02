from Meny import resources, MENU


def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return total


def report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")


def resources_check(coffee_type):
    water_needed = MENU[coffee_type]["ingredients"]["water"]
    coffee_needed = MENU[coffee_type]["ingredients"]["coffee"]
    milk_needed = MENU[coffee_type]["ingredients"].get("milk", 0)

    if resources["water"] < water_needed:
        print("Sorry there is not enough water.")
        return False
    if resources["coffee"] < coffee_needed:
        print("Sorry there is not enough coffee.")
        return False
    if milk_needed > 0 and resources["milk"] < milk_needed:
        print("Sorry there is not enough milk.")
        return False

    resources["water"] -= water_needed
    resources["coffee"] -= coffee_needed
    if milk_needed > 0:
        resources["milk"] -= milk_needed

    return True


def money_check(user_money, user_chose):
    if user_money < MENU[user_chose]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    elif user_money > MENU[user_chose]["cost"]:
        print("Here is ${:.2f} dollars in change.".format(user_money - MENU[user_chose]["cost"]))
        print("Here is your " + user_chose + ". Enjoy!")
    else:
        print("Here is your " + user_chose + ". Enjoy!")


def coffe(user_chose):
    if user_chose == "report":
        report()
    else:
        if resources_check(user_chose):
            total = money()
            money_check(total, user_chose)
        else:
            print("Sorry there is not enough resources.")
            return


print("What would you like? (espresso/latte/cappuccino):")
user_chosen = input()
do_you_want_next_coffe = True
while do_you_want_next_coffe:
    coffe(user_chosen)
    print("Do you want another coffe? (yes/no)")
    user_answer = input()
    if user_answer == "no".lower():
        do_you_want_next_coffe = False
    else:
        print("What would you like? (espresso/latte/cappuccino):")
        user_chosen = input().lower()
