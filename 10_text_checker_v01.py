# functions

# checks if input is text
def text_check(question):

    while True:

        error = "Please only enter text"

        response = input(question)
        valid = response.isalpha()

        if valid:
            return "*program continues"
        else:
            print(error)


# main routine
while True:
    text = text_check("Enter some text (no spaces or other characters EG: !@#$%): ")
    print(text)

