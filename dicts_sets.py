from ast import keyword
from optparse import Values


my_dicts_Nestle = {"KitKat" : "34,456,432 US Dollars",
"Nescafe" : "14,106,132 US Dollars",
 "Maggi" : "9,960,312 US Dollars", 
 "Nido" : "44,506,003 US Dollars",}
my_dicts_Unilever ={"Lipton ": "23,456,000 US Dollars",
"Breyers" : "1,235,891 US Dollars",
"HellManns" : "17,241,412 US Dollars",
"Marmite" : "11,715,324 US Dollars"}
for x in my_dicts_Nestle  :
        print(f"the Product is: {x} / Sales : {my_dicts_Nestle[x]}")
for s in my_dicts_Unilever:
    print(f"the Product is: {s} / Sales : {my_dicts_Unilever[s]}")

Nestle_products = len(my_dicts_Nestle.keys())
Unliever_products = len(my_dicts_Unilever.keys())
if Nestle_products > Unliever_products:
    print ("Nestle Has more products")
elif Unliever_products > Nestle_products :
    print("Unilever Has More Products")
else : print("they are equal")
the_top_product = max(my_dicts_Nestle.items() )
the_top_productU = max(my_dicts_Unilever.items())


#the_top_product = max(my_dicts_Nestle.items and my_dicts_Unilever.items())
print(f"the top product:{the_top_product[0]} in sales: {the_top_product[1]}")


#the_top_product = max(my_dicts_Nestle.items and my_dicts_Unilever.items())
print(f"the top product {the_top_productU[0]}in sales : {the_top_productU[1]}")

my_set_Nestle = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
my_set_Uliever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for x in my_set_Nestle | my_set_Uliever:
    print("this is print all sets: ",x)

for e in my_set_Nestle & my_set_Uliever :
    print("this all & sets: ",e)
for m in my_set_Nestle - my_set_Uliever:
    print("this is the Difference: ",m)    
 




