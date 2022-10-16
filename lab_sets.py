'''
Using what you've learned during . Please do the following :
'''
# Create a variable to hold the values of Nestle products (use a dicitionary)
nestle = {
    "KitKat": 34456432,
    "Nescafe": 14106132,
    "Maggi": 9960312,
    "Nido": 44506003}

# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever = {
    "Lipton": 23456000,
    "Breyers": 1235891,
    "HellManns": 17241412,
    "Marmite": 11715324}

print('-'*10)
# Print each product sold by Unilever and the sales figures / numbers for that product.
print("Products sold by Unilever: ")
for company, sales in unilever.items():
    print(f'\t - {company}: {sales:,} US Dollars.')
print('-'*10)

# Print each product sold by Nestle and the sales figures / numbers for that product.
print("Products sold by Nestle: ")
for company, sales in nestle.items():
    print(f'\t -{company}: {sales:,} US Dollars.')
print('-'*10)

# Print which of the companies has more products that the other company.
if len(nestle.keys()) > len(unilever.keys()):
    print("Nestle products are more than Unilever products.")
elif len(nestle.keys()) == len(unilever.keys()):
    print("Nestle and Unilever products are same numbers.")
else:
    print("Unilever products are more than Nestle products.")
print('-'*10)

# Print the top selling product from Nestle with sales figures.
nestle_most_sold_product_figure = 0
nestle_most_sold_product = None
for key, value in nestle.items():
    if value > nestle_most_sold_product_figure:
        nestle_most_sold_product_figure = value
        nestle_most_sold_product = key
print("The most sold product in Nestle:")
print(f"{nestle_most_sold_product}: \t{nestle_most_sold_product_figure:,} US Dollars")
print('-'*10)

# Print the top selling product from Unilever with sales figures.
print("The most sold product in Unilever:")
unilever_most_sold_product = max(unilever)
unilever_most_sold_product_figure = unilever[unilever_most_sold_product]
print(f"{unilever_most_sold_product}: {unilever_most_sold_product_figure:,} US Dollars")
print('-'*10)

nestle_countries: set = {"Saudi Arabia", "Oman",
                         "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries: set = {"Saudi Arabia", "Kuwait",
                           "Iraq", "Morocco", "Yemen", "United Emirates"}

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print(f"Cities both Unilever and Nestle sell their products in are :")
for i in nestle_countries | unilever_countries:
    print(f"\t - {i}")
print('-'*10)

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(f"Cities both Unilever and Nestle sell their products in common :")
for i in nestle_countries & unilever_countries:
    print(f"\t - {i}")
print('-'*10)

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(f"Cities that Nestle sell it's products in but Unilever doesn't :")
for i in nestle_countries - unilever_countries:
    print(f"\t - {i}")
print('-'*10)
