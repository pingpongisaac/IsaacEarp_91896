# functions

def yes_no(question):

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes or no")
            print()


def show_menu():
    print("*shows menu*")


# main routine
want_pizza = yes_no("Would you like to order a pizza?")

while want_pizza == "yes":

    show_menu()
    which_pizza = input("Which pizza would you like?")

    if which_pizza == "hawaiian":
        print("you chose hawaiian")
    elif which_pizza == "cheese":
        print("you chose plain cheese")
    elif which_pizza == "meatlovers":
        print("You chose meatlovers")
    elif which_pizza == "pepperoni":
        print("You chose pepperoni")
    else:
        print("Please enter a pizza from the menu")
        continue

    want_pizza = input("would you like to order another pizza?")
    if want_pizza == "yes":
        continue
    else:
        pass
