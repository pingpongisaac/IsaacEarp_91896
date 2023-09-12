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


# main routine
while True:
    want_instructions = yes_no("Do you want to see the instructions? ")

    if want_instructions == "yes":
        print("*shows instructions*")
        print("*program continues*")
        print()
    elif want_instructions == "no":
        print("*program continues*")
        print()
