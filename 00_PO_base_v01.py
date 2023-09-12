import pandas
import random

# functions


# show instructions
def show_instructions():
    print('''\n***** Instructions *****

For each ticket, enter...
- The person's name (can't be blank)
- Age (between 12 and 120)
- Payment method (cash / credit)

When you have entered all the users, press 'xxx' to quit.

The program will then display the ticket details
including the cost of each ticket, the total cost
and the total profit.

This information will automatically written to a text file.

***************************

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
    if var_pizza == "Hawaiian":
        price = 7

    # Plain Cheese Pizza is $6.50
    elif var_pizza == "Plain Cheese":
        price = 6.5

    # Meatlovers Pizza is $8.00
    elif var_pizza == "Meatlovers":
        price = 8

    # Pepperoni Pizza is $7.50
    else:
        price = 7.5

    return price


# calc toppings price function
def calc_toppings_price(var_toppings):

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
pizza_list = ["hawaiian", "plain cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "mushroom", "olives", "tomatoes"]

# dictionaries to hold pizza details
all_pizzas = []
all_pizza_costs = []
ind_topping = []
all_toppings = []
ind_topping_cost = []
all_toppings_cost = []

pizza_parlour_dict = {
    "[Pizza]": all_pizzas,
    "[Pizza Price]": all_pizza_costs,
    "[Extra Toppings]": all_toppings,
    "[Toppings Price]": all_toppings_cost
}


more_pizza = "yes"
toppings = 0

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
    pizza = string_checker("Please select which pizza you would like: ", 0, pizza_list).capitalize()

    if pizza == "Hawaiian":
        price = calc_pizza_price(pizza)
        print("You chose Hawaiian, that will be ${:.2f}".format(price))
    elif pizza == "Plain cheese":
        price = calc_pizza_price(pizza)
        print("You chose Plain Cheese, that will be ${:.2f}".format(price))
    elif pizza == "Meatlovers":
        price = calc_pizza_price(pizza)
        print("You chose Meatlovers, that will be ${:.2f}".format(price))
    elif pizza == "Pepperoni":
        price = calc_pizza_price(pizza)
        print("You chose Pepperoni, that will be ${:.2f}".format(price))
    # ensures program that price cannot be undefined, even though string checker will do
    # this any way
    else:
        price = 0

    pizza_cost = price
    topping_price = 0
    all_pizza_costs.append(pizza_cost)
    all_pizzas.append(pizza)

    want_toppings = string_checker("Would you like any extra toppings?", 1, yes_no_list)
    toppings = 0

    while want_toppings == "yes" and toppings < 2:

        show_toppings()
        topping = string_checker("What extra toppings would you like? (2 maximum)", 1, toppings_list).capitalize()
        if topping == "Ham":
            topping_price = topping_price + calc_toppings_price(topping)
            print("You have chosen Ham, that will be an extra ${:.2f}".format(topping_price))
        elif topping == "Mushroom":
            topping_price = topping_price + calc_toppings_price(topping)
            print("You have chosen Mushroom, that will be an extra ${:.2f}".format(topping_price))
        elif topping == "Olives":
            topping_price = topping_price + calc_toppings_price(topping)
            print("You have chosen Olives, that will be an extra ${:.2f}".format(topping_price))
        elif topping == "Tomatoes":
            topping_price = topping_price + calc_toppings_price(topping)
            print("You have chosen Tomatoes, that will be an extra ${:.2f}".format(topping_price))
        else:
            topping_price = 0
            topping = "none"

        toppings += 1
        ind_topping.append(topping)

        more_toppings = string_checker("Would you like any other toppings?", 1, yes_no_list)

        if more_toppings == "yes" and toppings > 1:
            print("You have already selected the maximum amount of toppings.")
            # add pizza and costs to lists
            pass
        elif more_toppings == "yes":
            pass
        elif more_toppings == "no":
            # add pizza and cost to lists
            break

    all_toppings.append(ind_topping)
    all_toppings_cost.append(topping_price)

    more_pizza = string_checker("Would you like to order another pizza?", 1, yes_no_list)
    if more_pizza == "yes":
        want_instructions = "no"
        pass
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

