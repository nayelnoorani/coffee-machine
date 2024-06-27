import accessmgt as am
import functions

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
