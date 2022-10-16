

Nestle_products = {"KitKat" : "34,456,432 US Dollars",
                  "Nescafe" : "14,106,132 US Dollars",
                    "Nido"  : "44,506,003 US Dollars",
                    "Maggi" : " 9,960,312 US Dollars"}

Unilever_products = {"Lipton" : "23,456,000 US Dollars",
                    "Breyers" : "1,235,891 US Dollars",
                  "HellManns" : "17,241,412 US Dollars",
                     "Marmite": "11,715,324 US Dollars"}


Nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_countries ={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}



#Print each product sold by Unilever and the sales figures / numbers for that product.
print("the product sold by Unilever and the sales: ")
print(list(Unilever_products.keys()) )
print(list( Unilever_products.values()) )
     
     

#Print each product sold by Nestle and the sales figures / numbers for that product.
print("product sold by Nestle and the sales: ")
print(list(Nestle_products.keys()))
print(list(Nestle_products.values()))


# Print which of the companies has more products that the other company.
if len(Nestle_products.keys()) > len (Unilever_products.keys()) :
    print("Nestle products has a more than Unilever products ")

elif len(Nestle_products.keys()) < len (Unilever_products.keys()):
     print("Unilever products has a more than Nestle products ")
else:
    print("there are same number of products")
    


# Print the top selling product from Nestle with sales figures.
Max_Nestle_products= max(Nestle_products, key=Nestle_products.get)
print("the top selling product from Nestle :",Max_Nestle_products)



# Print the top selling product from Unilever with sales figures.
Max_Unilever_Products = max(Unilever_products , key =Unilever_products.get)
print("the top selling product Unilever :" , Max_Unilever_Products)



#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in
city = set()
print("all the cities in Unilever & Nestl are:")
for city in Nestle_countries.union(Unilever_countries):
    print(city)



#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
cities = set()
print("cities that both Nestle & Unilver are:")
for cities in Nestle_countries.intersection(Unilever_countries):
    print(cities)



#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
diff_city = set()
print("cities Only Nestle sells in:")
for diff_city in Nestle_countries.difference(Unilever_countries):
    print(diff_city)