from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_work = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while machine_work:
    user_input = input(f"What would you like? {menu.get_items()}: ")

    if user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input == "off":
        machine_work = False
    elif menu.find_drink(user_input) is None:
        print(f"Please chose from this list and type is correctly - {menu.get_items()}")
    else:
        ingredients = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(ingredients):
            if money_machine.make_payment(ingredients.cost):
                coffee_maker.make_coffee(ingredients)
