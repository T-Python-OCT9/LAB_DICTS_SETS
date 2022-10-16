
Nestle_products = {"KitKat" : "34,456,432 US Dollars","Nescafe" : "14,106,132 US Dollars"
,"Maggi" : "9,960,312 US Dollars","Nido": "44,506,003 US Dollars"}
Unilever_products = {"Lipton" : "23,456,000 US Dollars","Breyers" :"1,235,891 US Dollars"
,"HellManns" : "17,241,412 US Dollars","Marmite" :"11,715,324 US Dollars"}


Nestl_city={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_city= {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


for key, value in Nestle_products.items():
    print(f"this is the Nestle Products{key}, and this is the sales numbers{value}")

for key, value in Unilever_products.items():
    print(f"this is the Nestle Products{key}, and this is the sales numbers{value}")

set_nestle = set (Nestle_products)
set_unilever = set (Unilever_products)

def more_products():
    if len(set_nestle)> len(set_unilever):
        print ("the Nestle has more products than unliever")
    elif len(set_nestle)< len(set_unilever):
        print ("the unliever has more products than Nestle")
    else:
        print ("they are the same")
    

'''Nestle_products2= {"KitKat" : "34,456,432","Nescafe" : "14,106,132"
,"Maggi" : "9,960,312","Nido": "44,506,003"}
Unilever_products2 = {"Lipton" : "23,456,000","Breyers" :"1,235,891"
,"HellManns" : "17,241,412","Marmite" :"11,715,324"}
def top_selling (x:dict):
    top :int = 0
    for i in float(x.values):
        if i> top: 
          top += i
    print(f"the top selling is : {top}")'''

def print_cities():
    all_cities = Nestl_city.union(Unilever_city)
    print(all_cities)
    

def common_cities():
    common_cities = Nestl_city.intersection(Unilever_city)
    print(common_cities)

def difference_cities():
    difference_cities = Nestl_city.difference(Unilever_city)
    print(difference_cities)

#top_selling(Nestle_products2)
more_products()
print_cities()
common_cities()
difference_cities()
