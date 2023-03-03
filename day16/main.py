from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_order():
    """Get order from user"""
    c_order = input(f"What would you like? ({menu.get_items()}): ")
    return c_order


def make_order(c_order):
    """Make order"""
    if c_order == 'off':
        return False
    elif c_order == 'report':
        coffee_maker.report()
        money_machine.report()
        return True
    else:
        drink = menu.find_drink(c_order)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        return True


is_on = True
while is_on:
    order = get_order()
    is_on = make_order(order)


