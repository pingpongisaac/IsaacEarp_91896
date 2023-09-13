import random
# function


def random_number():
    number = random.randint(1, 10)
    return number


# main routine
run_function = input("Run function?")

if run_function == "yes":
    while run_function == "yes":
        winner = random_number()

        if winner == 5:
            print("You have one a $20 Countdown gift card")
        else:
            print("You are not the winner")

        run_function = input("Run function?")
else:
    exit()
