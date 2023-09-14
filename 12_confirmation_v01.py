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


# show instructions
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

# lists for string checker referencing
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "mushroom", "olives", "tomatoes"]
delivery_pickup_list = ["delivery", "pickup"]

# dictionaries to hold pizza details
all_pizzas = []
all_pizza_costs = []
all_toppings = []
all_toppings_cost = []
temp_toppings = []

pizza_parlour_dict = {
    "[Pizza]": all_pizzas,
    "[Pizza Price]": all_pizza_costs,
    "[Extra Toppings]": all_toppings,
    "[Topping Price]": all_toppings_cost
}


more_pizza = "yes"
want_toppings = "no"
toppings_price = 0

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

        all_toppings.append(temp_toppings)
        all_toppings_cost.append(toppings_price)

        more_pizza = string_checker("Do you want any more pizzas?", 1, yes_no_list)

        if more_pizza == "yes":
            want_instructions = "no"
            continue
        elif more_pizza == "no":
            break

    pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)
    # pizza_parlour_frame = mini_movie_frame.set_index('Name')

    # calculate total ticket cost (ticket + surcharge)
    pizza_parlour_frame['[Total]'] = pizza_parlour_frame['[Pizza Price]'] + pizza_parlour_frame['[Topping Price]']

    order_total = pizza_parlour_frame['[Total]'].sum()
    winner = random_number()

    # Currency Formatting (uses currency function)
    add_dollars = ['[Pizza Price]', '[Topping Price]', '[Total]']
    for var_item in add_dollars:
        pizza_parlour_frame[var_item] = pizza_parlour_frame[var_item].apply(currency)

    print(pizza_parlour_frame)
    print()
    print("Your current order total comes to ${:.2f}".format(order_total))

    confirmation = string_checker("Would you like to confirm this order?", 1, yes_no_list)

    if confirmation == "yes":
        print("*program continues*")
    else:
        all_pizzas.clear()
        all_pizza_costs.clear()
        all_toppings.clear()
        all_toppings_cost.clear()
        pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)
        print(pizza_parlour_frame)

        print("Okay, you're order has been cancelled")

        new_order = string_checker("Would you like to begin another order?", 1, yes_no_list)

        if new_order == "yes":
            pass
        else:
            print("No worries, come back another day!")
            exit()

        more_pizza = "yes"
        continue

print()
print("Your order has been confirmed.")
print()
collection_method = string_checker("Would you like to have this order delivered (additional $5 fee) or for you to pick "
                                   "it up? (enter 'delivery' or 'pickup'): ", 0, delivery_pickup_list)

if collection_method == "delivery":
    print("You have chosen delivery, your new order total ${:.2f}".format(order_total + 5))
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
    print()
    print("You have chosen pick up")

if winner == 5:
    print("Congratulations, you are one our lucky %10 "
          "of customers. You have won a $20 Countdown gift card")
