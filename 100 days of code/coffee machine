MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {"water": 300, "milk": 200, "coffee": 100, 'money': 0}
turn_off = False
continue_1 = False

while not turn_off:

    # TODO: 1. ask user what they want to drink
    type_of_drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO: 2. turn off the machine
    if type_of_drink == "off":
        turn_off = True
        continue_1 = False
    # TODO: 3. print report
    elif type_of_drink == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")
        continue_1 = False
    # TODO: 4. check if there are enough resources

    elif type_of_drink in MENU:
        for ingredient in MENU[type_of_drink]["ingredients"]:
            if MENU[type_of_drink]["ingredients"][ingredient] > resources[ingredient]:
                print(f"Sorry there is not enough {ingredient}.")
                continue_1 = False
                break
            else:
                resources[ingredient] -= MENU[type_of_drink]["ingredients"][ingredient]
                continue_1 = True
    if continue_1:
        # TODO: 5. process coins and check transaction successful
        print("Please insert coins.")
        quarter = int(input("How many quarters: ")) * 0.25
        dime = int(input("How many dimes: ")) * 0.10
        nickle = int(input("How many nickles: ")) * 0.05
        penny = int(input("How many pennies: ")) * 0.01

        total = quarter + dime + nickle + penny
        resources['money'] += MENU[type_of_drink]['cost']
        if total < MENU[type_of_drink]['cost']:
            print("Sorry that's not enough money. Money refunded.")
            turn_off = False
        else:
            print(f"Here is ${round(total - MENU[type_of_drink]['cost'], 2)} in change.")
            print(f"Here is your {type_of_drink}☕. Enjoy!")
