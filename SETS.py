Kate = {"KitKat" : 34_456_432 , "Nescafe" : 14_106_132 , "Maggie" : 9_960_312 , "Nido" : 44_506_003}
Nadia = {"Lipton" : 23_456_000 , "Breyers " : 1_235_891  , "HellManns" : 17_241_412  , "Marmite" : 11_715_324 }

Nestle ={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


print ("Nestle Sold Products ...")
for i in Kate :  
 print (f"The product name is :{i} /{Kate[i]} US Dollars") 
 
print ("Unilever Sold Products ...") 
for x in Nadia :
 print (f"The product name is :{x} /{Nadia[x]} US Dollars")


if len(Kate)> len(Nadia):
    print("Nestle has more products")
elif  len(Nadia)> len(Kate):
    print("unilever has more products")
else :
    print ("They have the same products value")


top_selling=max(Kate,key=Kate.get)
print ("The top selling product in nestle is :",top_selling)

top_selling=max(Nadia,key=Nadia.get)
print ("The top selling product in Unilever is :",top_selling)

print(Nestle | Unilever)
print (Nestle & Unilever)
print (Nestle ^ Unilever)



