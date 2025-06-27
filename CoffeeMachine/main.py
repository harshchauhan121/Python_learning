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
resources["Money"]=0


while True:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=="off":
        break
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources["Money"]}")
    elif choice=="espresso":
        if MENU[choice]["ingredients"]["water"]<=resources["water"]:
            if MENU[choice]["ingredients"]["coffee"]<=resources["coffee"]:
                print("Please insert coins.")
                qtr=int(input("how many quarters?: "))
                dim=int(input("how many dimes?: "))
                nic=int(input("how many nickles?: "))
                pen=int(input("how many pennies?: "))
                money_paid= qtr*0.25 + dim*0.1 + nic*0.05 + pen*0.01
                if money_paid>=MENU[choice]["cost"]:
                    print(f"Here is ${round( money_paid-MENU[choice]["cost"] , 2 )} in change.")
                    resources["water"]-=MENU[choice]["ingredients"]["water"]
                    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                    resources["Money"]+= MENU[choice]["cost"]
                    print("Here is your espresso ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded! ")
            else:
                print("Sorry there is not enough coffee.")
        else:
            print("Sorry there is not enough water.")
    elif choice=="latte":
        if MENU[choice]["ingredients"]["water"]<=resources["water"]:
            if MENU[choice]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[choice]["ingredients"]["coffee"]<=resources["coffee"]:
                    print("Please insert coins.")
                    qtr=int(input("how many quarters?: "))
                    dim=int(input("how many dimes?: "))
                    nic=int(input("how many nickles?: "))
                    pen=int(input("how many pennies?: "))
                    money_paid= qtr*0.25 + dim*0.1 + nic*0.05 + pen*0.01
                    if money_paid>=MENU[choice]["cost"]:
                        print(f"Here is ${round( money_paid-MENU[choice]["cost"] , 2 )} in change.")
                        resources["water"]-=MENU[choice]["ingredients"]["water"]
                        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                        resources["Money"]+= MENU[choice]["cost"]
                        print("Here is your latte ☕️. Enjoy!")
                    else:
                        print("Sorry that's not enough money. Money refunded! ")
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")
    elif choice=="cappuccino":
        if MENU[choice]["ingredients"]["water"]<=resources["water"]:
            if MENU[choice]["ingredients"]["milk"] <= resources["milk"]:
                if MENU[choice]["ingredients"]["coffee"]<=resources["coffee"]:
                    print("Please insert coins.")
                    qtr=int(input("how many quarters?: "))
                    dim=int(input("how many dimes?: "))
                    nic=int(input("how many nickles?: "))
                    pen=int(input("how many pennies?: "))
                    money_paid= qtr*0.25 + dim*0.1 + nic*0.05 + pen*0.01
                    if money_paid>=MENU[choice]["cost"]:
                        print(f"Here is ${round( money_paid-MENU[choice]["cost"] , 2 )} in change.")
                        resources["water"]-=MENU[choice]["ingredients"]["water"]
                        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                        resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                        resources["Money"]+= MENU[choice]["cost"]
                        print("Here is your cappuccino ☕️. Enjoy!")
                    else:
                        print("Sorry that's not enough money. Money refunded! ")
                else:
                    print("Sorry there is not enough coffee.")
            else:
                print("Sorry there is not enough milk.")
        else:
            print("Sorry there is not enough water.")






