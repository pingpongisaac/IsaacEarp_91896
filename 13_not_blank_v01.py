# function goes here

# checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question)

        # if the response is blank, outputs error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# main routine
address = not_blank("Please enter your address")

print("You entered your address as {}, is this correct?".format(address))
