import colorama
from colorama import init, Fore, Back, Style

colorama.init(autoreset=True)

from datetime import datetime

menu = {
    "Tea": 1.00,
    "Americano": 1.70,
    "Latte": 1.90,
    "Cappuccino": 1.90,
    "Mocha": 2.00,
    "Hot chocolate": 2.20,
    "Croissant": 1.50,
    "Muffin": 2.10,
    "Toast": 1.00,
    "Panini": 2.90,
    "Buttered Roll": 0.70,
    "Stroopwafel": 0.50
}

extras = {
    "Skimmed milk": 0.15,
    "2% milk": 0.20,
    "Full fat milk": 0.30,
    "Almond milk": 0.35,
    "Oat milk": 0.35,
    "Soya milk": 0.35,
    "Lactose-free milk": 0.40,
    "Custard": 1.00,
    "Ham 1 slice": 0.50,
    "Shredded chicken": 1.50,
    "Butter": 0.30,
    "Cheese": 1.00,
    "Salami 1 slice": 0.50,
    "Salad": 0.70
}
final_order = []
def start():
    while True:
        customer_name = input("Hello and welcome to Brian's Bistro, please can I take your name: ")
        current_datetime = datetime.now().strftime("%d-%m-%Y-- %H:%M:%S")
        menu = print("""Unfortunately our card machine is broken today and we are only accepting cash. Here is the menu
        " Drinks              Food
            
        - Tea           : £1.00  │ - Croissant     : £1.50  
        - Americano     : £1.70  │ - Muffin        : £2.10  
        - Latte         : £1.90  │ - Toast         : £1.00  
        - Cappuccino    : £1.90  │ - Panini        : £2.90  
        - Mocha         : £2.00  │ - Buttered Roll : £0.70  
        - Hot Chocolate : £2.20  │ - Stroopwafel   : £0.50  
        - Bottled Water : £1.00  │ - Potato Cake   : £1.00  )

        welcome_message = input("Would you like to place an order y/n: """)
        if welcome_message == "y":
            print(Back.WHITE+ Fore.BLACK+"Good choice")
        elif welcome_message == "n":
            start()
        else:
            print("Invalid input, enter 'y' or 'n' ")
        break



    total_cost = 0
    while True:
            order_input = input(Back.WHITE+ Fore.BLACK+"What would you like to order?: ").capitalize()
            if order_input.capitalize() not in menu:
                print(Fore.RED + "Sorry, that item is not available.")
                continue
            order_count = int(input(Back.WHITE+ Fore.BLACK+"How many would you like: "))
            total_cost += menu[order_input] * order_count
            print(Fore.GREEN + f"{order_count} {order_input}(s) have been added to your order. Current total: £{total_cost:.2f}")
            final_order.append(order_input)

            extra_order = input(Back.WHITE+ Fore.BLACK+"Would you like to add any extras? (y/n): ")
            if extra_order.lower() == 'y':
                print("Available extras:")
                for extra in extras:
                    print(f"- {extra}: £{extras[extra]:.2f}")
                while True:
                    chosen_extra = input("Enter the name of the extra you'd like to add, or 'finished' to finish: ").capitalize()
                    if chosen_extra == 'Finished':
                        break
                    elif chosen_extra in extras:
                        total_cost += extras[chosen_extra]
                        print(Fore.GREEN + f"{chosen_extra} has been added to your order. Current total: £{total_cost:.2f}")
                    else:
                        print(Fore.RED + "Sorry, that extra is not available.")
            elif extra_order.lower() != 'n' and extra_order.lower() != 'y':
                print(Fore.RED + "Invalid input. Please enter 'y' or 'n'.")

            next_order = input("Would you like to add another item to you order? (y/n) or 'restart' to cancel all items and start again: ")
            if next_order.lower() == 'n':
                break
            elif next_order.lower() == 'restart':
                total_cost = 0
                start()

    final_order_str = str(final_order)

    with open("receipts.txt", "a", encoding="utf-8") as f:
            f.write(f"{customer_name} - Order: {(final_order_str)} - Total: £{total_cost:.2f} - Date and Time: {current_datetime}\n")
            f.close()
            f = open("receipts.txt", "r")
            print(f.read())

    print(Fore.BLUE + f"Here is your order {customer_name} The total is £{total_cost:.2f}. Thank you for visiting Brian's Bistro, have a good day")
    print(Fore.BLUE + f"Date and Time: {current_datetime}")    

start()