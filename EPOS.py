# import classes
import datetime

from itemsforsale import ItemsForSale, Menu, Drink, Food
from time import gmtime, strftime

# instantiate all drinks with correct name and price

d1 = Drink("Tea", 1)
d2 = Drink("Americano", 1.7)
d3 = Drink("Latte", 1.9)
d4 = Drink("Cappucino", 1.9)
d5 = Drink("Mocha", 2)
d6 = Drink("Hot Chocolate", 2.2)

# instantiate all food with correct name and price

f1 = Food("Croissant", 1.5)
f2 = Food("Muffin", 2.1)
f3 = Food("Toast", 1)
f4 = Food("Panini", 2.9)
f5 = Food("Buttered Roll", 0.7)
f6 = Food("Stroopwafel", 0.5)

# instantiate Menu objetc with name and max number of items

m1 = Menu("Megabytes", 30)

#  add all drink objetcs to drimk dictionary

m1.add_drink(d1)
m1.add_drink(d2)
m1.add_drink(d3)
m1.add_drink(d4)
m1.add_drink(d5)
m1.add_drink(d6)

#  add all food objetcs to drimk list


#  add all food objetcs to drimk list

m1.add_food(f1)
m1.add_food(f2)
m1.add_food(f3)
m1.add_food(f4)
m1.add_food(f5)
m1.add_food(f6)

print("Welcome to Megabyte.")
user_name = input("What is your name?: ").capitalize()
print(f"Hi {user_name}! Have a look at our menu")


# init file
        

actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())
filename = user_name + " - " + str(actual_time) + ".txt"

outfile = open(filename, "w")
# with open('orders.txt', 'a') as outfile:
outfile.write('\n')
outfile.write('\n')
outfile.write(f"Order made by: {user_name}\n")
outfile.write('\n')
outfile.write("megabytes Order")
outfile.write('\n')
outfile.write(str(datetime.datetime.now()))
outfile.write('\n')
outfile.close()

# init global vars
total_food_cost = 0
total_drink_cost = 0


# Define function to show food menu
def show_food(menu_items):
    print("\nFood Menu:")
    for i, food_item in enumerate(menu_items, start=1):
        print(f"{i}. {food_item.name} - £{food_item.price}")

# Define function to show drink menu
def show_drinks(menu_items):
    print("\nDrink Menu:")
    for i, drink_item in enumerate(menu_items, start=1):
        print(f"{i}. {drink_item.name} - £{drink_item.price}")

# Print the menu options
show_food(m1.food_items)
show_drinks(m1.drinks)

# Define function to take food order
def take_food_order(menu_items):
    global total_food_cost
    food_order = []
    food_cost = 0
    food_quantity= []                                          
    counter = 0                                                 
    # total_food_cost = 0                                         
    # Loop to take food orders
    while True:
        # Prompt user to select an item
        item_num = input("Enter the food item number to order (enter 0 to finish): ")
        if item_num == '0':
            break
        elif item_num.isdigit() and 1 <= int(item_num) <= len(menu_items):

            # Add selected item to the order
            food_item = menu_items[int(item_num) - 1]
            food_order.append(food_item)
            # IMPORTANT place in while loop for integrity
            
            food_quantity_input = input("How many do you want?    ")
            
            if food_quantity_input.isdigit()>0 and food_quantity_input.isdigit()<7:
                
                food_quantity.append(food_quantity_input)                 
                food_cost = food_item.price * float(food_quantity[counter])                 
                total_food_cost += round(float(food_cost),3)                                                
                counter += 1 
                print("Would you like to order anything else?")      
              
            else:
                print("Invalid item number. Please try again.")
    print("\nYour Food Order:")
    for i, item in enumerate(food_order, start=1):
         print(f"{i}. {item.name}, x{food_quantity[ i-1 ]} - £{item.price}") 
         with open(filename, 'a') as outfile:
            outfile.write('\n')
            outfile.write(item.name)    
            outfile.write('\n')
            outfile.write("Quantity  ")
            outfile.write(str(food_quantity[ i-1 ]))
            outfile.write('\n')
            outfile.write("Item price  ")
            outfile.write(str(item.price))
            outfile.write('\n')


    print(f"Total Cost: £{total_food_cost}")
    with open(filename, 'a') as outfile:
        # outfile.write('\n')
        outfile.write("Total Food Cost is  £")
        outfile.write(str(total_food_cost))
        outfile.write('\n')
### QUESTION have we got this twice, test         
    # print(f"The order cost is {total_food_cost} ")
    print(datetime.datetime.now())


# Define function to take drink order
def take_drink_order(menu_items):
    global total_drink_cost
    drink_order = []
    drink_cost = 0
    drink_quantity= []                                          
    counter = 0                                                 
    # total_drink_cost = 0                                        
    # Loop to take drink orders
    while True:
        # Prompt user to select an item
        item_num = input("Enter the drink item number to order (enter 0 to finish): ")
        if item_num == '0':
            break
        elif item_num.isdigit() and 1 <= int(item_num) <= len(menu_items):
            # Add selected item to the order
            drink_item = menu_items[int(item_num) - 1]
            drink_order.append(drink_item)
            drink_quantity_input = input("How many do you want?    ")
            if drink_quantity_input.isdigit()>0 and drink_quantity_input.isdigit()<7:
                drink_quantity.append(drink_quantity_input)                            
            drink_cost = drink_item.price * float(drink_quantity[counter])                 
            total_drink_cost += (round(float(drink_cost),3))                                               
            counter += 1  
            print("Would you like to order anything else?")
            drink_cost += (drink_item.price)
        else:
            print("Invalid item number. Please try again.")


    print("\nYour Drink Order:")
    ### QUESTION should we open the file here and write the following to the file instead of the current method?
    for i, item in enumerate(drink_order, start=1):
      with open(filename, 'a') as outfile:
        outfile.write('\n')
        outfile.write(item.name)    
        outfile.write('\n')
        outfile.write("Quantity  ")
        outfile.write(str(drink_quantity[ i-1 ]))
        outfile.write('\n')
        outfile.write("Item price  ")
        outfile.write(str(item.price))
        outfile.write('\n')

        print(f"{i}. {item.name}, x{drink_quantity[ i-1 ]} - £{item.price}")   ### QUESTION SHOULD THIS BE IN THE LOOP LIKE FOOD
    print(f"Total Cost: £{total_drink_cost}")
    with open(filename, 'a') as outfile:
      # outfile.write('\n')
      outfile.write("Total Drink Cost is  £")
      # outfile.write('\n')
      outfile.write(str(total_drink_cost))             ### WRITE TO FILE ?
    
# Prompt user to order


# Loop to handle orders

start_order = input("\nWhat would you like to order? (1 for Food) or (2 for Drinks) (enter '0' to exit): ")
while start_order != "0":
    if start_order == "1":
        # Take food order
        take_food_order(m1.food_items)
    elif start_order == "2":
        # Take drink order
        take_drink_order(m1.drinks)
    else:
        print("Invalid option. Please enter '1' for food, '2' for drinks, or '0' to exit.")

    # Prompt user again for their order
    start_order = input("\nWould you like to order anything else? (1 for Food) or (2 for Drinks) (enter '0' to exit): ")


total_order_value =  total_drink_cost + total_food_cost
print(f"\nTotal Order Cost: {total_order_value}")
with open(filename, 'a') as outfile:
   outfile.write('\n')
   outfile.write("Total Order Cost is  £")
   outfile.write(str(total_order_value))
   outfile.write('\n')



print(f"Thank you for your order {user_name}!")
file1 = open(filename, "r")
print(file1.read())
file1.close() 
