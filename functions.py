from art import logo
import resourcemgt as rm

def main_screen():
    print(logo)
    print("What would you like to do?")
    print("Type '1' to order coffee")
    print("Type '2' to manage the machine")
    print("Type 'off' to turn off the machine")
    user_input = input(">> ")
    return user_input

# Functions allowing maintenance of the coffee machine

function_options = ["report", "load resources", "collect coins"]

def maintenance_screen():
    print("What would you like to do?")
    for i, option in enumerate(function_options):
        print(f"{i+1}. {option}")
    user_input = int(input(">> "))
    return function_options[user_input-1]

def print_report():
    print(f"Water: {rm.resources['water']}ml")
    print(f"Milk: {rm.resources['milk']}ml")
    print(f"Coffee: {rm.resources['coffee']}g")
    print(f"Money: ${(rm.calculate_value(**rm.coins)):.2f}")

def load_resources():
    print("Which resource would you like to add? Type the number corresponding to your choice.")
    for i in range(len(rm.resources)):
        print(f"{i+1}. {list(rm.resources.keys())[i]}")
    user_input = int(input(">> "))
    loaded_amount = int(input("How much? "))
    rm.resources[list(rm.resources.keys())[user_input-1]] += loaded_amount
    print(f"{loaded_amount} {list(rm.resources.keys())[user_input-1]} added.")

def empty_coins():
    print(f"Current balance is ${(rm.calculate_value(**rm.coins)):.2f}")
    for key, value in rm.coins.items():
        print(f"{key}: {value}")
    confirmation = input("Are you sure you want to empty all coins? (y/n): ").lower() == 'y'
    if confirmation:
        print("Coins emptied.")
        rm.coins = {key: 0 for key in rm.coins}

# Functions allowing users to order coffee
def order_coffee():
    menu_options = [key for key in rm.MENU.keys()]
    print("What would you like to order? Type the number corresponding to your choice.")
    for i in range(len(menu_options)):
        print(f"{i+1}. {menu_options[i]}")
    user_input = int(input(">> "))
    order_cost = rm.MENU[menu_options[user_input-1]]['cost']
    print(f"Your order of one {menu_options[user_input-1]} costs ${order_cost:.2f}.")
    return menu_options[user_input-1]

def check_resources(coffee):
    ingredients = rm.MENU[coffee]['ingredients']
    insufficient_ingredients = [key for key in ingredients if ingredients[key] > rm.resources[key]]

    if not insufficient_ingredients:
        return True
    else:
        print(f"Sorry, there is not enough {', '.join(insufficient_ingredients)}.")
        return False

# Cashier function - collects coins, checks for difference between cost and payment, and returns change or logs payment
def process_payment(coffee):
    cost = rm.MENU[coffee]['cost']
    print("Please insert coins.")
    coins = [key for key in rm.coins.keys()]
    amounts = [int(input(f"How many {coin}?: ")) for coin in coins]
    total_paid = rm.calculate_value(*amounts)
    difference = total_paid - cost
    if difference >= 0:
        if difference > 0:
            print(f"Thank you for the tip of ${difference:.2f}.")
        for coin, amount in zip(coins, amounts):
            rm.coins[coin] += amount
        return True
    elif difference < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(coffee):
    ingredients = rm.MENU[coffee]['ingredients']
    for key in ingredients:
        rm.resources[key] -= ingredients[key]
    print(f"Here is your {coffee} ☕. Enjoy!")
