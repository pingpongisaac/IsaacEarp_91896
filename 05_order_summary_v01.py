import pandas
# functions


def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid response"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def calc_pizza_price(var_pizza):

    if var_pizza == "hawaiian":
        price = 7.50
    elif var_pizza == "cheese":
        price = 6.00
    elif var_pizza == "pepperoni":
        price = 7.00
    elif var_pizza == "meatlovers":
        price = 8.50
    else:
        price = 0

    return price


def calc_topping_price(var_topping):

    if var_topping == "ham":
        price = 2.00
    elif var_topping == "olives":
        price = 2.00
    elif var_topping == "onion":
        price = 1.50
    elif var_topping == "tomatoes":
        price = 2.50
    elif var_topping == "mushroom":
        price = 3.50
    else:
        price = 0

    return price


# main routine
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "olives", "onion", "tomatoes", "mushroom"]

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

toppings_price = 0

want_pizza = string_checker("Would you order a pizza?", 1, yes_no_list)

while want_pizza == "yes":

    which_pizza = string_checker("What pizza would you like?", 1, pizza_list)
    print("You chose {} for ${}".format(which_pizza, calc_pizza_price(which_pizza)))
    all_pizzas.append(which_pizza)
    all_pizza_costs.append(calc_pizza_price(which_pizza))

    want_toppings = string_checker("Would you like any extra toppings?", 1, yes_no_list)
    toppings_price = 0
    temp_toppings = []

    if want_toppings == "yes":
        while want_toppings == "yes":
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
pizza_parlour_frame['[Total]'] = pizza_parlour_frame['[Pizza Price]'] + pizza_parlour_frame['[Topping Price]']

order_total = pizza_parlour_frame['[Total]'].sum()


print(pizza_parlour_frame)
print()
print("Your order total is ${}".format(order_total))
