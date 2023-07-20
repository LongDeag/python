from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_off = False
menu = Menu()
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()

while not turn_off:
    order = input(f"What would you like? ({menu.get_items()}): ")
    menu_item = menu.find_drink(order)
    if order == "off":
        turn_off = True
    elif order == "report":
        coffe_maker.report()
        money_machine.report()

    else:
        check_resources = coffe_maker.is_resource_sufficient(menu_item)
        if check_resources:
            transaction_successful = money_machine.make_payment(menu_item.cost)
            if transaction_successful:
                coffe_maker.make_coffee(menu_item)

