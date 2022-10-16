# LAB_DICTS_SETS

### Kate, Dalia & Monica are work associates . They all work at a consultancy company.

## Kate has the products sales of Nestle :

##### KitKat : 34,456,432 US Dollars
##### Nescafe : 14,106,132 US Dollars
##### Maggi : 9,960,312 US Dollars
##### Nido : 44,506,003 US Dollars

      

## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars
      

## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
'''- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.
- Print the top selling product from Nestle with sales figures.
- Print the top selling product from Unilever with sales figures.
- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.'''


nestle_products = {"KitKat" : "34,456,432 US Dollars", "Nescafe" : "14,106,132 US Dollars", "Maggi" : "9,960,312 US Dollars", "Nido" : "44,506,003 US Dollars"}

unilever_products = {"Lipton" : "23,456,000 US Dollars", "Breyers" : "1,235,891 US Dollars", "HellManns" : "17,241,412 US Dollars", "Marmite" : "11,715,324 US Dollars"}

nestle_total_sales = 0
for n in nestle_products:
    print("The number of " + n + " Products is: " + nestle_products[n])
    nestle_total_sales = nestle_total_sales + int(nestle_products[n])

unilever_total_sales = 0
for u in unilever_products:
    print("The number of " + u + " Products is: " + unilever_products[u])
    unilever_total_sales = unilever_total_sales + int(unilever_products[u])

if len(nestle_products) > len(unilever_products):
    print("Nestle has more products than Unilever")
elif len(nestle_products) < len(unilever_products):
    print("Unilever has more products than Nestle")
else:
    print("They are the same nubmer of products")


def the_top_seller():
    if nestle_total_sales > unilever_total_sales:
        print("Nestle has the top sales total by: " + nestle_total_sales + " nubmer of sales")
    else:
        print("Unilever has the top sales total by: " + unilever_total_sales + " nubmer of sales")

the_top_seller()



nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

uni_add_nes_countries = nestle_countries.union(unilever_countries)

for i in uni_add_nes_countries:
    print("this is all the cities Unilever & Nestle sell their products in:- ")
    print("-" + i)


uni_and_nes_countries = nestle_countries.intersection(unilever_countries)
for x in uni_and_nes_countries:
    print("this is the countries that both Nestle & Unilver sell in common:-")
    print("-" + x)

nes_diff_uni_countries = nestle_countries.difference(unilever_countries)

for y in nes_diff_uni_countries:
    print("this is the cities Nestle sells in , but Unilver doens't sell in:-")
    print("-" + y)
