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
    print('''\n********** Menu **********
 1: Hawaiian Pizza: $7.00
 2: Cheese Pizza: $6.50
 3: Meatlovers: $8.00
 4: Pepperoni: $7.50
**************************''')


# main routine
want_pizza = yes_no("Would you like to order a pizza?")

while want_pizza == "yes":

    show_menu()
    which_pizza = input("Which pizza would you like?")

    if which_pizza == "1":
        print("you chose hawaiian")
    elif which_pizza == "2":
        print("you chose plain cheese")
    elif which_pizza == "3":
        print("You chose meatlovers")
    elif which_pizza == "4":
        print("You chose pepperoni")
    else:
        print("Please enter a pizza from the menu")
        continue

    want_pizza = input("would you like to order another pizza?")
    if want_pizza == "yes":
        continue
    else:
        pass
