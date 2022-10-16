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

Nestle_sales_list = {34456432 , 14106132 , 9960312, 44506003 }
print(" The highest selling product in Nestle is : ")

def printing_the_top_nes_sales():
    for top in Nestle_sales_list:
        if top == max(Nestle_sales_list):
            print(top,"US Dollars")

Unilever_sales_list = { 23456000, 1235891, 17241412, 11715324 }
print(" The highest selling product in Unilever is: ")

def printing_the_top_uni_sales():
    for top in Unilever_sales_list:
        if top == max(Unilever_sales_list):
            print(top, "US Dollars")


nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

uni_add_nes_countries = nestle_countries.union(unilever_countries)

def printing_the_uni():
    for i in uni_add_nes_countries:
        print("-" + i)


uni_and_nes_countries = nestle_countries.intersection(unilever_countries)
def printing_the_intersec():
    for x in uni_and_nes_countries:
        print("-" + x)

nes_diff_uni_countries = nestle_countries.difference(unilever_countries)

def printing_the_diff():
    for y in nes_diff_uni_countries:
        print("-" + y)

printing_the_top_nes_sales()
printing_the_top_uni_sales()
print("this is all the cities Unilever & Nestle sell their products in:- ")
printing_the_uni()
print("this is the countries that both Nestle & Unilver sell in common:-")
printing_the_intersec()
print("this is the cities Nestle sells in , but Unilver doens't sell in:-")
printing_the_diff()