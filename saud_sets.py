
kate_products_Nestle = {
"KitKat" : 34_456_432 ,
"Nescafe" : 14_106_132 ,
"Maggi" : 9_960_312 ,
"Nido" : 44_506_003 }
dalia_products_unilever = {
"Lipton":23_456_000 ,
"Breyers":1_235_891 ,
"HallManns":17_241_412 ,
'Marmite':11_715_324 }


nestle_countries = {
"Saudi Arabia", "Oman"
, "Kuwait", "Egypt", 
"Jordan", "Sudan"}
unilver_countries = {
"Saudi Arabia","Kuwait", 
"Iraq", "Morocco", 
"Yemen", "United Emirates"}

print("Products sold by Nestle:")
for products, pris in kate_products_Nestle.items():
    print({products:[pris]})

print("------------------------------")

print("Products sold by unilver")   
for product , pris in dalia_products_unilever.items():
    print({product},[pris])


print(" which companies has more products that the other company") 

if len(dalia_products_unilever) > len(kate_products_Nestle):
   print("dalia has more product")
elif len(kate_products_Nestle) > len(dalia_products_unilever):
    print("kate has more product")
else :
    print("has the same produce")
print("------------------------------")
print("what the top selling product from Nestle")
top_selling_product_from_Nestle = {"KitKat" : 34_456_432 ,
"Nescafe" : 14_106_132 ,
"Maggi" : 9_960_312 ,
"Nido" : 44_506_003 }

print(max(top_selling_product_from_Nestle))

top_selling_product_from_unilever = {"Lipton":23_456_000 ,
"Breyers":1_235_891 ,
"HallManns":17_241_412 ,
'Marmite':11_715_324 }
print("what the top selling product from unilever")
print(max(top_selling_product_from_unilever))
print("------------------------------")

print("all cities sling product")
set_of_all_cities_in_nestle_unilever = nestle_countries.union (unilver_countries)
print(set_of_all_cities_in_nestle_unilever)

print("cities that both Nestle & Unilver sell in common")
set_of_both = nestle_countries & unilver_countries
print(set_of_both)

print(" cities Nestle sells in , but Unilver doens't sell in")
set_of_cities_dont_seel_in = nestle_countries.difference(unilver_countries)
print(set_of_cities_dont_seel_in)


