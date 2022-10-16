"""

This is the 10th lab 
which is about Dictionaries and Sets :D 

"""

Nestle_Products = {"34,456,432 US Dollars": "KitKat", "14,106,132 US Dollars": "Nescafe", "9,960,312 US Dollars": "Maggi", "44,506,003 US Dollars": "Nido"}
Unilever_Products = {"23,456,000 US Dollars": "Lipton", "1,235,891 US Dollars": "Breyers", "17,241,412 US Dollars": "HellManns", "11,715,324 US Dollars": "Marmite"}

#Unpacking the Values of Nestle to kate list
Kate_products = list(Nestle_Products.values())
#print(f"Kate Products are : {Kate_products}")

#Unpacking the Values of Unilever to Dalia list
Dalia_products = list(Unilever_Products.values())
#print(f"Dalia Products are : {Dalia_products}")

#Monica has 2 tables containing the countries in which Unilever and Nestle sell the products
Nestle_Containing_Country = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_Containing_Country = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

Monica_Country_List = Nestle_Containing_Country | Unilever_Containing_Country

#print(f"Monica list about containing countries are : {Monica_Country_List}")

# Print each product sold by Unilever and the sales figures / numbers for that product.

print("Products sold by Unilever are : ", list(Unilever_Products.items()))

#Print each product sold by Nestle and the sales figures / numbers for that product.

print("Products sold by Nestle are : ", list(Nestle_Products.items()))

#Print which of the companies has more products that the other company.

if len(Nestle_Products) > len(Unilever_Products):
    print("Nestle has more products than Unilever")
elif  len(Nestle_Products) < len(Unilever_Products): 
    print("Unilever has more products than Nestle") 
else:
    print("Both companies has same Products")

#Print the top selling product from Nestle with sales figures.  
Nestle_list = {34456432 , 14106132 , 9960312, 44506003 }
print(" The highest selling product in Nestle is : ")

for top in Nestle_list:
    if top == max(Nestle_list):
        print(top," US Dollars")

#Print the top selling product from Unilever with sales figures.
Unilever_list = { 23456000, 1235891, 17241412, 11715324 }
print(" The highest selling product in Unilever is : ")
for top in Unilever_list:
    if top == max(Unilever_list):
        print(top, "US Dollars")

#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.

Nestle_Unilever_sells = Nestle_Containing_Country | Unilever_Containing_Country
print("All the countries that Nestle & Unilever sells in are :")
for Country in Nestle_Unilever_sells:
    print(Country)

#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.

Nestle_unilever_common = Nestle_Containing_Country & Unilever_Containing_Country

print("The common countries that both Nestle & Unilever sells in are: ")
for common in Nestle_unilever_common:
    print(common)

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.

Nestle_but_notUnilever = Nestle_Containing_Country - Unilever_Containing_Country

print(" Countries Nestle sells in but Unilever doesnt are : ")

for onlyNestle in Nestle_but_notUnilever:
    print(onlyNestle)