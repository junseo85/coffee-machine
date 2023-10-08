from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
machine_money = MoneyMachine()
coffee = Menu()

machine_working = True
while machine_working == True:
    user_order = input("What would you like? (espresso/latte/cappuccino): ")
    if user_order == "off":
        machine_working = False
    elif user_order == "report":
        machine.report()
        machine_money.report()
    else:
        information = coffee.find_drink(user_order)
        if machine.is_resource_sufficient(coffee.find_drink(user_order)) == True:
            if machine_money.make_payment(information.cost):
                machine.make_coffee((information))