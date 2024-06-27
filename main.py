import accessmgt as am
import functions

# DONE 1: Switch machine on. While on, offer choice of "Menu Options", "Function Options" or "Power Off"

# TODO 2: If user selects function option, ask for secret password, then print list from function_options
# TODO 2a: If user selects report, print current resources from resources dict
# TODO 2b: If user selects load, ask for load amount and update resources dict
# TODO 2c: If user selects collect coins, print report of coins, confirm collection and empty coins dict

# DONE 3: If user selects menu option, print list from menu_options
# DONE 3a: Check resources for adequate materials to produce user's order
# DONE 3b: Inform user of cost of their order and process coins deposited (separate function)
# DONE 3b: If resources adequate & payment completed, deduct resource cost of order and update resources dict

# DONE 4: Process payments - function to calculate the dollar value of coins


# DONE 4a: Ask user for coins being inserted and calculate the value paid. Update coins dict for each coin
# DONE 4b: Calculate excess (value) and refund coins if user overpays, inform of shortfall if user underpays


# DONE 5: If user selects power off, switch machine off

machine_on = input("Would you like to turn on the coffee machine? (y/n): ").lower() == 'y'

while machine_on:
    user_input = functions.main_screen()

    if user_input == '1':
        # display menu and ask for order
        coffee_order = functions.order_coffee()
        # check if resources are adequate
        if functions.check_resources(coffee_order):
            # process payment
            if functions.process_payment(coffee_order):
                # deliver coffee
                functions.make_coffee(coffee_order)

    elif user_input == '2':
        # authenticate user
        if am.authenticate_user():
            maintenance_action = functions.maintenance_screen()

            if maintenance_action == 'report':
                functions.print_report()

            elif maintenance_action == 'load resources':
                functions.load_resources()
            
            elif maintenance_action == 'collect coins':
                functions.collect_coins()
            
            else:
                print("Invalid input. Please try again.")

    elif user_input == 'off':
        machine_on = False
    
    else:
        print("Invalid input. Please try again.")