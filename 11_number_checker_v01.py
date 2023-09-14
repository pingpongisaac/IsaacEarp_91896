# functions

# checks if input is on consisting of numbers
def num_check(question):

    while True:

        error = "Please only enter numbers"

        response = input(question)
        valid = response.isnumeric()

        if valid:
            return "*program continues*"
        else:
            print(error)


# main routine
while True:
    number = num_check("Enter a number (in numeric form EG:1234): ")
    print(number)
