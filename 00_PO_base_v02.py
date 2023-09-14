import pandas
import random
from datetime import date

# functions


# checks if input is text
def text_check(question):

    while True:

        error = "Please only enter text"

        response = input(question)
        valid = response.isalpha()

        if valid:
            return response
        else:
            print(error)


# checks if input is on consisting of numbers
def num_check(question):

    while True:

        error = "Please only enter numbers"

        response = input(question)
        valid = response.isnumeric()

        if valid:
            return response
        else:
            print(error)


# shows instructions
def show_instructions():
    print('''\n********** Instructions **********

To order a pizza, type in the pizza you would like from the menu.
Only the first word is necessary when entering the pizza 
eg: Cheese Pizza would simply require "cheese".

To order a topping, you would similarly enter the topping from the menu you desire.
eg: If you wanted Ham as an extra topping, you would enter "ham"

After you choose the desired pizzas with any extra toppings,
your order will be organised into a summary presented at the end of your order.

This information will also be automatically written to a text file, as a receipt.

**************************************

Here is the menu:''')


# shows menu of pizzas
def show_menu():
    print('''\n********** Menu **********
 * Hawaiian Pizza: $7.00
-------------------------- 
 * Cheese Pizza: $6.50
-------------------------- 
 * Meatlovers: $8.00
--------------------------     
 * Pepperoni: $7.50
**************************''')


# shows menu of toppings
def show_toppings():
    print('''\n******* Toppings *******
 * Ham: $2.50
------------------------
 * Mushroom: $3.50
------------------------
 * Onion: $1.50
 ----------------------- 
 * Olives: $2.00
------------------------
 * Tomatoes: $2.50
************************''')


# calc pizza price function
def calc_pizza_price(var_pizza):

    # Hawaiian Pizza is $7.00
    if var_pizza == "hawaiian":
        price = 7

    # Plain Cheese Pizza is $6.50
    elif var_pizza == "cheese":
        price = 6.5

    # Meatlovers Pizza is $8.00
    elif var_pizza == "meatlovers":
        price = 8

    # Pepperoni Pizza is $7.50
    else:
        price = 7.5

    return price


# calc toppings price function
def calc_topping_price(var_toppings):

    # Ham is $1.50
    if var_toppings == "ham":
        price = 2.5

    # Mushroom is $2.00
    elif var_toppings == "mushroom":
        price = 2

    # Olives are $1.50
    elif var_toppings == "olives":
        price = 1.5

    # Tomatoes are $2.00
    else:
        price = 2

    return price


# validates string based on list of options
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid input"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# currency format
def currency(x):
    return "${:.2f}".format(x)


# random winner
def random_number():
    number = random.randint(1, 10)
    return number


# main routine goes here

# lists to hold items for string checker
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "mushroom", "olives", "tomatoes"]
delivery_pickup_list = ["delivery", "pickup"]
payment_list = ["cash", "card"]

# declaration of lists for order summary
all_pizzas = []
all_pizza_costs = []
all_toppings = []
all_toppings_cost = []
temp_toppings = []

# headings for columns of order summary
pizza_parlour_dict = {
    "[Pizza]": all_pizzas,
    "[Pizza Price]": all_pizza_costs,
    "[Extra Toppings]": all_toppings,
    "[Topping Price]": all_toppings_cost
}

# basic declarations needed to initiate program
more_pizza = "yes"
want_toppings = "no"
toppings_price = 0

# Introductory/customer details sequence
print("Welcome to Isaac's Pizza Parlour!")
print()
name = text_check("Please enter your name for your order: ")
print()
phone = num_check("Hello {}, can we please have your phone number for if we need to contact you: ".format(name))
print()
want_instructions = string_checker("Thank you! Would you like to read the "
                                   "instructions for how to use our system? "
                                   "(yes/no): ", 1,
                                   yes_no_list)

# pizza ordering loop
while True:
    while more_pizza == "yes":
        if want_instructions == "yes":
            show_instructions()
            show_menu()
        else:
            print()
            print("Okay, here is the menu:")
            show_menu()

        print()

        # initial pizza selection
        which_pizza = string_checker("Please select which pizza you would like: ", 0, pizza_list)
        print()
        print("You chose {} for ${:.2f}".format(which_pizza, calc_pizza_price(which_pizza)))

        # appends items into order summary
        all_pizzas.append(which_pizza)
        all_pizza_costs.append(calc_pizza_price(which_pizza))
        print()
        want_toppings = string_checker("Would you like any extra toppings?", 1, yes_no_list)
        toppings_price = 0
        temp_toppings = []

        # runs through toppings order loop to determine toppings
        if want_toppings == "yes":
            while want_toppings == "yes":
                show_toppings()
                print()
                which_topping = string_checker("What toppings would you like?", 1, toppings_list)
                print()
                print("You chose {} for ${:.2f}".format(which_topping, calc_topping_price(which_topping)))

                # prepares items for order summary
                toppings_price = toppings_price + calc_topping_price(which_topping)
                temp_toppings.append(which_topping)

                print()
                want_toppings = string_checker("Would you like any more extra toppings?", 1, yes_no_list)

                if want_toppings == "yes":
                    continue
                elif want_toppings == "no":
                    break
        else:
            temp_toppings.append("None")

        # appends items into order summary
        all_toppings.append(temp_toppings)
        all_toppings_cost.append(toppings_price)

        more_pizza = string_checker("Do you want any more pizzas?", 1, yes_no_list)

        if more_pizza == "yes":
            want_instructions = "no"
            continue
        elif more_pizza == "no":
            break

    # order summary = data frame of dictionary items
    pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)

    # calculates total pizza and toppings for each item on order summary
    pizza_parlour_frame['[Total]'] = pizza_parlour_frame['[Pizza Price]'] + pizza_parlour_frame['[Topping Price]']

    # configures order total and random winner of gift card
    order_total = pizza_parlour_frame['[Total]'].sum()
    winner = random_number()

    # currency formatting (uses currency function)
    add_dollars = ['[Pizza Price]', '[Topping Price]', '[Total]']
    for var_item in add_dollars:
        pizza_parlour_frame[var_item] = pizza_parlour_frame[var_item].apply(currency)

    # show user order summary
    print()
    print(pizza_parlour_frame)
    print()
    print("Your current order total comes to ${:.2f}".format(order_total))

    # code to confirm that the user would like to proceed with order
    print()
    confirmation = string_checker("Would you like to confirm this order?", 1, yes_no_list)

    if confirmation == "yes":
        break
    else:
        all_pizzas.clear()
        all_pizza_costs.clear()
        all_toppings.clear()
        all_toppings_cost.clear()
        pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)

        print()
        print("Okay, you're order has been cancelled")
        print()
        new_order = string_checker("Would you like to begin another order?", 1, yes_no_list)

        if new_order == "yes":
            pass
        else:
            print()
            print("No worries, come back another day!")
            exit()

        more_pizza = "yes"
        continue

print()
print("Your order has been confirmed.")
print()
collection_method = string_checker("Would you like to have this order delivered (additional $5 fee) or for you to pick "
                                   "it up? (enter 'delivery' or 'pickup'): ", 0, delivery_pickup_list)

# determines collection method for user (delivery or pick up)
if collection_method == "delivery":
    order_total = order_total + 5
    print("You have chosen delivery, your new order total ${:.2f}".format(order_total))
    print()
    while True:
        address = input("Please enter your address for delivery: ")
        print()
        correct_address = string_checker("You have entered your address as '{}' is this correct?".format(address), 1, yes_no_list)

        if correct_address == "yes":
            break
        else:
            continue
else:
    address = "pickup"
    print()
    print("You have chosen pick up")

payment_method = string_checker("What payment method would you like to use (cash or card (5% surcharge))?", 0, payment_list)

if payment_method == "card":
    order_total = order_total * 1.05
    print()
    print("You chose card, that will be a 5% surcharge, for a new order total of ${:.2f}. You "
          "can pay this when you pickup/receive your delivery.".format(order_total))
else:
    print()
    print("You chose cash, your order total remains {}. You can pay"
          "this when you pickup/receive your delivery.".format(order_total))
    pass

print()
if collection_method == "delivery":
    print("Thank you for ordering with Isaac's Pizza Parlour, your pizza will arrive in 15-20 minutes. "
          "Please contact us if there are any delays: 0800 154 4634.")
elif collection_method == "pickup":
    print("Thank you for ordering with Isaac's Pizza Parlour, your pizza will be ready for pick up in 10-15"
          "minutes.")

# tells winner if they won a gift card
if winner == 5:
    print("Surprise! You are one our lucky %10 "
          "of customers. You have won a $20 Countdown gift card")

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "--------------- Isaac's Pizza Parlour Receipt ({}/{}/{}) --------------\n".format(day, month, year)
filename = "{}_pizza_order_{}_{}_{}".format(name, year, month, day)

# address the user
address_customer = "Order for {}\n" \
                   "Ph: {}\n" \
                   "{}\n".format(name, phone, address)

items_ordered_heading = "----------------------------- Items Ordered -----------------------------\n"
# Change frame to a string so that we can export it to file
pizza_parlour_string = pandas.DataFrame.to_string(pizza_parlour_frame)

# create strings for printing....
total_order_heading = "\n------------------------------ Order Total ------------------------------\n"
total_order_price = "Your total order price is: ${:.2f}\n".format(order_total)

# closing statement
thank_you = "Thank you for ordering from Isaac's Pizza Parlour, enjoy your meal!"

# list holding content to print \ write to file
to_write = [heading, address_customer, items_ordered_heading,
            pizza_parlour_string, total_order_heading, total_order_price,
            thank_you]


# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
