import pandas
import random

# functions


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


# show menu
def show_menu():
    print('''\n********** Menu **********
 * Hawaiian Pizza: $7.00
 * Cheese Pizza: $6.50
 * Meatlovers: $8.00
 * Pepperoni: $7.50
**************************''')


# show toppings menu
def show_toppings():
    print('''\n********** Toppings **********
 * Ham: $2.50
 * Mushroom: $2.00
 * Olives: $1.50
 * Tomatoes: $2.00
*****************************''')


# checks if input is integer
def num_check(question):

    while True:

        try:
            response = int(input(question))
            return response

        except ValueError:
            print("Please enter an integer.")


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


# cash / credit based on list of options
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


# main routine goes here

# lists for string checker referencing
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "mushroom", "olives", "tomatoes"]

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
    "[Toppings Price]": all_toppings_cost
}


more_pizza = "yes"
want_toppings = "no"
toppings_price = 0

want_instructions = string_checker("Would you like to read the "
                                   "instructions? (y/n): ", 1,
                                   yes_no_list)

while more_pizza == "yes":
    if want_instructions == "yes":
        show_instructions()
        show_menu()
    else:
        print("Okay, here is the menu:")
        print()
        show_menu()

    print()

    # initial pizza selection
    which_pizza = string_checker("Please select which pizza you would like: ", 0, pizza_list).capitalize()

    print("You chose {} for ${}".format(which_pizza, calc_pizza_price(which_pizza)))
    all_pizzas.append(which_pizza)
    all_pizza_costs.append(calc_pizza_price(which_pizza))

    want_toppings = string_checker("Would you like any extra toppings?", 1, yes_no_list)
    toppings_price = 0
    temp_toppings = []

    if want_toppings == "yes":
        while want_toppings == "yes":
            show_toppings()
            which_topping = string_checker("What toppings would you like?", 1, toppings_list)
            print("You chose {} for ${}".format(which_topping, calc_topping_price(which_topping)))
            toppings_price = toppings_price + calc_topping_price(which_topping)
            temp_toppings.append(which_topping)
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
        continue
    elif more_pizza == "no":
        break


pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)
# pizza_parlour_frame = mini_movie_frame.set_index('Name')

# calculate total ticket cost (ticket + surcharge)
pizza_parlour_frame['[Total]'] = pizza_parlour_frame['[Pizza Price]'] \
                            + pizza_parlour_frame['[Toppings Price]']

order_total = pizza_parlour_frame['[Total]'].sum()

# Currency format
add_dollars = ['[Pizza Price]', '[Toppings Price]', '[Total]']
for var_item in add_dollars:
    pizza_parlour_frame[var_item] = pizza_parlour_frame[var_item].apply(currency)

print(pizza_parlour_frame)
print()
print("Your order total comes to ${:.2f}".format(order_total))

