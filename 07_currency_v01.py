import pandas
# functions


# currency formatting function
def currency(x):
    return "${:.2f}".format(x)


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
