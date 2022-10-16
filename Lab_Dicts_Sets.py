
#Dectionaries
Nestle_Products = {
    "KitKat" : 34456432 ,
    "Nescafe" : 14106132 , 
    "Maggi" : 9960312 ,
    "Nido" : 44506003 ,
}

Unilever_Products = {
    "Lipton" : 23456000 ,
    "Breyers" : 1235891 ,
    "HellManns" : 17241412 ,
    "Marmite" : 11715324 ,
}

#Sets
Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"} 
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}



print("-------- All products sold by Unilever ----------")
for key , value in Unilever_Products.items():
    print(key , value ," US Dollars")

print("-------- All products sold by Nestle ----------")
for key , value in Nestle_Products.items():
    print(key , value ," US Dollars")


print("----------- which of the companies has more products that the other company -------------")
if len(Nestle_Products) > len(Unilever_Products) :
    print(" Nestle has more products ")
elif len(Nestle_Products) < len(Unilever_Products) :
    print(" Unilever has more products ")
else :
    print("Nestle and Unilever have the same number of products")


print("------------------------------")
Nestle_max = max(Nestle_Products, key=Nestle_Products.get )
Nestle_max_num = Nestle_Products.values()
Nestle_max_value = max(Nestle_max_num)
print("Top selling product from Nestle : ", Nestle_max ,"  and It's price ",Nestle_max_value, "US Dollars")

Unilever_max = max(Unilever_Products, key=Unilever_Products.get)
Unilever_max_num = Unilever_Products.values()
Unilever_max_value = max(Unilever_max_num)
print("Top selling product from Unilever : ", Unilever_max ," and It's price",Unilever_max_value, "US Dollars")


print("------------------------------")
print("All the countries Unilever & Nestle sell their products in : ")
for val in Nestle | Unilever :
    print(" ", val)

print("------------------------------")
print("print the countries that both Nestle & Unilver sell in common : ")
for val in Nestle & Unilever :
    print(" ", val)

print("------------------------------")
print("print the countries Nestle sells in , but Unilver doens't sell in : " )
for val in Nestle - Unilever :
    print(" ", val)