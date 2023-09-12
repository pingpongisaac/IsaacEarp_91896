# functions

def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid response"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


def show_menu():
    print("*shows menu*")


# main routine
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
toppings_list = ["ham", "olives", "onion", "tomatoes", "mushroom"]

want_pizza = string_checker("Would you like to order a pizza?", 1, yes_no_list)

if want_pizza == "no":
    exit()

while want_pizza == "yes":

    show_menu()
    which_pizza = input("Which pizza would you like?")
    print("You chose", which_pizza)

    want_toppings = string_checker("Would you like extra toppings?", 1, yes_no_list)

    if want_toppings == "no":
        pass

    while want_toppings == "yes":
        which_toppings = string_checker("Which toppings would you like?", 1, toppings_list)
        print("You chose", which_toppings)

        want_toppings = string_checker("Would you like any more extra toppings?", 1, yes_no_list)

    want_pizza = string_checker("Would you like to order another pizza?", 1, yes_no_list)

    if want_pizza == "yes":
        continue
