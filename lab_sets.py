'''
Using what you've learned during . Please do the following :
'''
# Create a variable to hold the values of Nestle products (use a dicitionary)
nestle = {
    "KitKat": "34,456,432 US Dollars",
    "Nescafe": "14,106,132 US Dollars",
    "Maggi": "9,960,312 US Dollars",
    "Nido": "44,506,003 US Dollars"}

# Create a variable to hold the values of Unilever products (Use a dictionary)
unilever = {
    "Lipton": "23,456,000 US Dollars",
    "Breyers": "1,235,891 US Dollars",
    "HellManns": "17,241,412 US Dollars",
    "Marmite": "11,715,324 US Dollars"}


# Print each product sold by Unilever and the sales figures / numbers for that product.
for company, sales in unilever.items():
    print(f'The Unilever sales of {company} is: \t{sales}.')

# Print each product sold by Nestle and the sales figures / numbers for that product.
for company, sales in nestle.items():
    if company == 'Nescafe':
        print(f'The Nestle sales of {company} is: \t{sales}.')
    else:
        print(f'The Nestle sales of {company} is: \t\t{sales}.')

# Print which of the companies has more products that the other company.
if len(nestle.keys()) > len(unilever.keys()):
    print("Nestle products are more than Unilever products.")
elif len(nestle.keys()) == len(unilever.keys()):
    print("Nestle and Unilever products are same numbers.")
else:
    print("Unilever products are more than Nestle products.")

# Print the top selling product from Nestle with sales figures.
nestle_top_product = max(nestle.items())
print(
    f"Nestle top selling product is {nestle_top_product[0]} which sales are: \t\t{nestle_top_product[1]}")

# Print the top selling product from Unilever with sales figures.
unilever_top_product = max(unilever.items())
print(
    f"Nestle top selling product is {unilever_top_product[0]} which sales are:\t\t {unilever_top_product[1]}")


nestle_countries: set = {"Saudi Arabia", "Oman",
                         "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries: set = {"Saudi Arabia", "Kuwait",
                           "Iraq", "Morocco", "Yemen", "United Emirates"}

# Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print(f"Cities both Unilever and Nestle sell their products in are :")
for i in nestle_countries | unilever_countries:
    print(f"\t - {i}")

# Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print(f"Cities both Unilever and Nestle sell their products in common :")
for i in nestle_countries & unilever_countries:
    print(f"\t - {i}")

# Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print(f"Cities that Nestle sell it's products in but Unilever doesn't :")
for i in nestle_countries - unilever_countries:
    print(f"\t - {i}")
