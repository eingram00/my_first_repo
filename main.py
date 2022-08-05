# Imports
import menu


def check_resources(wat, cof, mil, cost):
    if wat > menu.resources['water']:
        print("Not enough water")
        return
    elif cof > menu.resources['coffee']:
        print("Not enough coffee")
        return
    elif mil > menu.resources['milk']:
        print("Not enough milk")
        return
    
    print(f"Your drink costs ${cost}, please insert coins")
    quarter = int(input("How many quarters: "))
    dime = int(input("How many dimes: "))
    nickle = int(input("How many nickles: "))
    penny = int(input("How many pennies: "))
    total_coin = ((25 * quarter) + (10 * dime) + (5 * nickle) + (1 * penny))/100

    if total_coin < cost:
        print("Not enough money")
        return
    elif total_coin > cost: 
        change = total_coin - cost
        print(f"Here's your change: ${change}")
        return cost
    else:
        return cost


def machine_report(money_in):
    print(f"water: {menu.resources['water']}ml")
    print(f"milk: {menu.resources['milk']}ml")
    print(f"coffee: {menu.resources['coffee']}g")
    print(f"money: ${money_in}")


def make_coffee(coffee):
    '''Makes the Coffee'''
    if coffee == "espresso":
        water_amount = menu.MENU[coffee]['ingredients']['water']
        coffee_amount = menu.MENU[coffee]['ingredients']['coffee']
        milk_amount = 0
        #print(f"Water: {water_amount}, Coffee: {coffee_amount}, Milk: {milk_amount}")
    else:
        water_amount = menu.MENU[coffee]['ingredients']['water']
        coffee_amount = menu.MENU[coffee]['ingredients']['coffee']
        milk_amount = menu.MENU[coffee]['ingredients']['milk']
        #print(f"Water: {water_amount}, Coffee: {coffee_amount}, Milk: {milk_amount}")
    
    drink_cost = menu.MENU[coffee]['cost']
    money = check_resources(water_amount, coffee_amount, milk_amount, drink_cost)
    return money


def machine_start():
    machine_on = True
    money = 0

    while machine_on:

        # User prompt
        user_choice = input("What would you like? espresso/latte/cappuccino: ")

        # Turn Off Coffee Machine
        if user_choice == "off":
            machine_on = False

        # Print Report
        elif user_choice == "report":
            machine_report(money)

        # Make the Coffee
        else:
            money += make_coffee(user_choice)
            print(f"Here's your {user_choice}, Enjoy!")


# Go Time
machine_start()