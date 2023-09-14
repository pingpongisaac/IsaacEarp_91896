import pandas
import random
from datetime import date
# functions


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# produce random number
def random_number():
    number = random.randint(1, 10)
    return number


# main routine

# dictionaries to hold ticket details
all_pizzas = ["hawaiian", "cheese", "meatlovers", "pepperoni"]
all_pizza_costs = [7.50, 6.50, 8.50, 7.50]
all_toppings = ["[onion]", "[ham, olives]", "[tomatoes, mushroom]", "none"]
all_toppings_cost = [1.50, 4.00, 6.00, 0.00]


pizza_parlour_dict = {
    "[Pizzas]": all_pizzas,
    "[Pizza Price]": all_pizza_costs,
    "[Toppings]": all_toppings,
    "[Topping Price]": all_toppings_cost
}

name = "isaac"
phone = "0800838383"
address = "123 Pizza Street"
pizza_parlour_frame = pandas.DataFrame(pizza_parlour_dict)

pizza_parlour_frame['[Total]'] = pizza_parlour_frame['[Pizza Price]'] + \
                                pizza_parlour_frame['[Topping Price]']

order_total = pizza_parlour_frame['[Pizza Price]'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['[Pizza Price]', '[Topping Price]', '[Total]']
for var_item in add_dollars:
    pizza_parlour_frame[var_item] = pizza_parlour_frame[var_item].apply(currency)

print(pizza_parlour_frame)
print()
print("Your order total is ${:.2f}".format(order_total))

# **** Get current date for heading and filename ****
# get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

heading = "--------------- Isaac's Pizza Parlour Receipt ({}/{}/{}) --------------\n".format(day, month, year)
filename = "{}_pizza_order_{}_{}_{}".format(name, year, month, day)

# address the user
address_customer = "Order for {}\n" \
                   "Ph: {}\n" \
                   "{}\n".format(name, phone, address)

items_ordered_heading = "----------------------------- Items Ordered -----------------------------\n"
# Change frame to a string so that we can export it to file
pizza_parlour_string = pandas.DataFrame.to_string(pizza_parlour_frame)

# create strings for printing....
total_order_heading = "\n------------------------------ Order Total ------------------------------\n"
total_order_price = "Your total order price is: ${:.2f}\n".format(order_total)

# closing statement
thank_you = "Thank you for ordering from Isaac's Pizza Parlour, enjoy your meal!"

# list holding content to print \ write to file
to_write = [heading, address_customer, items_ordered_heading,
            pizza_parlour_string, total_order_heading, total_order_price,
            thank_you]


# write output to file
# create file to hold data (add .txt extension)
write_to = "{}.txt".format(filename)
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
