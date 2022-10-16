Nestle_Products_Sales = {"KitKat" : 34_456_432, "Nescafe": 14_106_132 ,"Maggi": 9_960_312 , "Nido":44_506_003}
Unilever_Products_Sales = {"Lipton" :23_456_000, "Breyers": 1_235_891,"HellManns":17_241_412, "Marmite":11_715_324}
Nestle_countries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilever_countries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print("-"*10)

print("This is each proudct sold by Unilever and it's sales figures : ")
for key,value in Unilever_Products_Sales.items():
    print(f"{key}: {value} US Dollars")

print("-"*10)

print("This is each proudct sold by Nestle and it's sales figures : ")
for key,value in Nestle_Products_Sales.items():
    print(f"{key}: {value} US Dollars")

print("-"*10)
 
if len (Nestle_Products_Sales)>len(Unilever_Products_Sales):
    print("Nestle has more products")
elif len(Unilever_Products_Sales) > len(Nestle_Products_Sales):
    print("Unilver has more products")
else:
    print("Unilver and Nestle has the same products amount...")

print("-"*10)

#top selling product from Nestle and Unilever with sales figures
print( "The top selling product in Nestle is : ",max(Nestle_Products_Sales))    
print( "The top selling product in Unilever is : ",max(Unilever_Products_Sales)) 
print("-"*10)

#all the countries Unilever & Nestle sell their products in.
print("The countries that Unilever and Nestle both sell thier products in : ",Unilever_countries | Nestle_countries)
print("-"*10)

#countries both Nestle & Unilver sell in common.
print("The countries that Unilever and Nestle both sell in common : ",Unilever_countries & Nestle_countries)
print("-"*10)

#countries Nestle sells in , but Unilver doens't sell in.
print("The countries that Nestle sell in but Unilever doens't : ",Nestle_countries - Unilever_countries)

