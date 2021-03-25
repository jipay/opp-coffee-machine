from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

commands = [
    "report",
    "off",
    "espresso",
    "latte",
    "cappuccino",
    "credit",
]

menu = Menu()
moneybags = MoneyMachine()
maker = CoffeeMaker()
alive = True


def print_report():
    global maker
    global moneybags
    maker.report()
    moneybags.report()


def turn_off():
    global alive
    alive = False


while alive:
    cmd = input(f"What would you like? ({menu.get_items()}): ")
    if cmd == "off":
        turn_off()
    elif cmd == "report":
        print_report()
    else:
        drink = menu.find_drink(cmd)
        if maker.is_resource_sufficient(drink):
            if moneybags.make_payment(drink.cost):
                maker.make_coffee(drink)


