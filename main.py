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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
water = 300
milk = 200
coffee = 100
money = 0

machine_working = True
while machine_working:
    user_item = input("What would you like? (espresso/latte/cappuccino): ")

    def ingredients(user_item):
        """check the item's ingredients and see if machine can make the product"""
        global water, coffee, milk, machine_working
        if user_item == "espresso":
            item_water = MENU[user_item]["ingredients"]["water"]

            item_coffee = MENU[user_item]["ingredients"]["coffee"]
            if water < item_water and coffee < item_coffee:
                machine_working = False
                return
            elif water < item_water:
                print("Sorry there is not enough water.")
                return
            elif coffee < item_coffee:
                print("Sorry there is not enough coffee.")
                return
            else:
                water -= item_water
                coffee -= item_coffee
        else:
            item_water = MENU[user_item]["ingredients"]["water"]

            item_coffee = MENU[user_item]["ingredients"]["coffee"]
            item_milk = MENU[user_item]["ingredients"]["milk"]
            if water < item_water and coffee < item_coffee:
                machine_working = False
                return

            elif water < item_water:
                print("Sorry there is not enough water.")
                return

            elif coffee < item_coffee:
                print("Sorry there is not enough coffee.")
                return
            elif milk < item_milk:
                print("Sorry there is not enough milk.")
                return
            else:
                water -= item_water
                coffee -= item_coffee
                milk -= item_milk
        price = MENU[user_item]["cost"]
        price_check(money, user_item, price)

    def price_check(coin, item, cost):
        """check and calculate the money"""
        print("Please insert coins.")
        quarters = int(input("how many quarters?:")) * 0.25
        dimes = int(input("how many dimes?:")) * 0.10
        nickles = int(input("how many nickles?:")) * 0.05
        pennies = int(input("how many pennies?:")) * 0.01
        total = quarters + dimes + nickles + pennies

        if total < cost:
            print("Sorry that's not enough money. Money refunded")

        else:
            global money
            money = coin + cost
            change = total - cost
            change = round(change, 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {item} ☕. Enjoy!")


    if user_item == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${money}")

    elif user_item == "off":
        machine_working = False

    else:
        ingredients(user_item)





