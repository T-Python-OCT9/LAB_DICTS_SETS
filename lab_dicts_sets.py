# - Create a variable to hold the values of Nestle products (use a dicitionary)
Nestle_products = {"KitKat": 34456432, "Nescafe": 14106132,
                   "Maggi": 9960312, "Nido": 44506003}

# Create a variable to hold the values of Unilever products (Use a dictionary)
Unilever_products = {"Lipton": 23456000, "Breyers": 1235891,
                     "HellManns": 17241412, "Marmite": 11715324}
# - Print each product sold by Unilever and the sales figures / numbers  for that product.
for key, value in Unilever_products.items():
    print(f"{key}:{value} US Dollars ")

print(f"the sales of Unilever: {Unilever_products}")
# - Print each product sold by Nestle and the sales figures / numbers  for that product.
for key, value in Nestle_products.items():
    print(f"{key}:{value} US Dollars ")

print(f"the sales of  Nestle: { Nestle_products}")
# - Print which of the companies has more products that the other company.
len_Unilever = len(Unilever_products)
print(len_Unilever)
len_Nestle = len(Nestle_products)
print(len_Nestle)
# - Print which of the companies has more products that the other company.
if len_Nestle > len_Unilever:
    print("Nestle has more products")
elif len_Unilever > len_Nestle:
    print("Unilever has more products")
else:
    print("Nestle and Unilever has same number products")
# - Print the top selling product from Nestle with sales figures.
print(f"the top selling in Nestle is {max(Nestle_products)}")
# - Print the top selling product from Unilever with sales figures.
print(f"the top selling in Unilever is {max(Unilever_products)}")
# - Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
# - Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq",
            "Morocco", "Yemen", "United Emirates"}
print(Unilever.union(Nestle))
print(Unilever.intersection(Nestle))
print(Unilever.difference(Nestle))
union_value = {x for x in Unilever | Nestle}
print(union_value)
intersection_value = {x for x in Unilever & Nestle}
print(intersection_value)
difference_value = {x for x in Unilever - Nestle}
print(difference_value)


