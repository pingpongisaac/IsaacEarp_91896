# functions


# string checker to check valid responses
def string_checker(question, num_letters, valid_responses):

    error = "Please choose a valid response"

    while True:
        response = input(question).lower()

        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        print(error)


# main routine
yes_no_list = ["yes", "no"]
pizza_list = ["hawaiian", "cheese", "meatlovers", "pepperoni"]

while True:
    which_pizza = string_checker("Which pizza would you like?", 1, pizza_list)
    print("You chose", which_pizza)
    want_instructions = string_checker("Would you like to see the instructions?", 1, yes_no_list)
    print("You chose", want_instructions)


