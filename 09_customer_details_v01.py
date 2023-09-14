# functions

# checks if input is on consisting of numbers
def num_check(question):

    while True:

        error = "Please only enter numbers"

        response = input(question)
        valid = response.isnumeric()

        if valid:
            return response
        else:
            print(error)


# checks if input is text
def text_check(question):

    while True:

        error = "Please only enter text"

        response = input(question)
        valid = response.isalpha()

        if valid:
            return response
        else:
            print(error)


# main routine

name = text_check("What is your name for the order?")
phone = num_check("What is your phone number in case we need to contact you?")
address = input("What is your address for the delivery?")

print("Name = ", name)
print("Phone = ", phone)
print("Address = ", address)
