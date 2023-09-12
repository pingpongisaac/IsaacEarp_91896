# functions

def string_checker(question, num_letters, valid_responses):

    error = "That seems wrong, could you please try again?"

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
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "olives", "onion", "tomatoes", "mushroom"]


while True:
    which_pizza = string_checker("What pizza would you like?", 1, pizza_list)
    print("You chose {} for ${}".format(which_pizza, calc_pizza_price(which_pizza)))

    which_topping = string_checker("What toppings would you like?", 1, toppings_list)
    print("You chose {} for ${}".format(which_topping, calc_topping_price(which_topping)))




