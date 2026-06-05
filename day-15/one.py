from secrets import choice

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,

}


def is\


    _resource\_sufficient():
is \_enough = True
for item in order\_ingredients:
    order\_ingredients\[item] >= resources\[item]:
print(f"sorry there is no enough {item}")
is \_enough = False
return is \_enough


def process\


    _coins():
print("please insert coins")
total = int(input("how many quarters:"))\*0.25
total += int(input("how many dimes:")) \*0.1
total += int(input("how many nickels:")) \*0.05
total += int(input("how many pennies:")) \*0.01
return total


def is\


    _transaction\_successful(money\_received, drink\_cost):
if money\_received >= drink\_cost:
    change = round(money\_received - drink\_cost, 2)
    print(f"here is your change \${change}")
    global profit
    profit += drink\_cost
    return True
    else:
    print("there is no enough amount given! money refunded")
    return False

    is \_on = True
    while is \_on:
        choice = input("What would you like?(espresso/latte/cappuccino):")
    if choice == "off":
        is \_on = False
    elif choice == "report":
        print(f"Water:{resources\["water"]}ml")
    print(f"Milk:{resources\["milk"]}ml")

    ```
    print(f"Coffee:{resources["coffee"]}ml")
    print(f"Money:${profit}")
    else:
    drink = MENU[choice]
    if is_resource_sufficient(drink["ingredients"]):
        payment = process_coins()
        is_transaction_successful(payment, drink["cost"])

    ```
