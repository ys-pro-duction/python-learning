MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def print_report():
    print(f"""
    ===== REPORT =======
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${money}
    ====================
    """)


def is_resources_available(coffee_name):
    coffee_ingredient = MENU[coffee_name]["ingredients"]
    for key in coffee_ingredient:
        if resources[key] - coffee_ingredient[key] < 0:
            print(f"Sorry there is not enough {key}.")
            return False
    return True


def collect_money(coffee_name):
    cost = MENU[coffee_name]["cost"]
    print(f"{coffee_name} cost is ${cost}\nEnter coins")
    quarter = int(input("quarter 0.25 x "))
    dimes = int(input("dimes 0.10 x "))
    nickel = int(input("nickel 0.05 x "))
    pennies = int(input("pennies 0.01 x "))
    return (quarter * 0.25) + (dimes * 0.1) + (nickel * 0.05) + (pennies * 0.01)


def process_coffee(coffee_name, coin):
    coffee = MENU[coffee_name]
    if coffee["cost"] > coin:
        print("Sorry that's not enough money. Money refunded.")
        return
    coffee_ingredient = coffee["ingredients"]
    for key in coffee_ingredient:
        resources[key] -= coffee_ingredient[key]
    global money
    money += coffee["cost"]
    change = coin - coffee["cost"]
    if change > 0:
        print(f"Here is ${round(change, 2)} dollars in change.")
    print(f"Here is your {coffee_name}☕. Enjoy!")


is_machine_on = True
money = 0

while is_machine_on:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_choice == "off":
        print("machine off for maintenance")
        break
    elif coffee_choice == "report":
        print_report()
        continue
    if is_resources_available(coffee_choice):
        coins = collect_money(coffee_choice)
        process_coffee(coffee_choice, coins)
    else:
        print(f"Resources are not available for {coffee_choice}.")
