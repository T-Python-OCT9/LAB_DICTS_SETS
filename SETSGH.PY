# this is the SETS lab - 16 oct - ghadah alahrbi 
from pickle import FALSE


nestle_products= {"KitKat ": 34456432 ,"Nescafe" : 14106132 ,"Maggi": 9960312 ,"Nido" : 44506003}

unilever_products={"Lipton" : 23456000, "Breyers" : 1235891, "HellManns" : 17241412, "Marmite" : 11715324}

#printing 
print("the products of unilever ")
for key,value in unilever_products.items():
    print(f"{key}:{value} US Dollar")

print("the products of nestle ")
for key,value in nestle_products.items():
    print(f"{key}:{value} US Dollar")
# who has more products 

if len(nestle_products) > len(unilever_products):

    print("nestle has more products than unilever")

elif len(nestle_products) < len(unilever_products) :

   print("unilever has more products than nestle") 

else:
    print("unilever and nestle has the same number of products ")

# Printing the top selling product from Nestle with sales figures

def get_key(v, my_dict):
    for key, value in my_dict.items():
        if v == value:
            return key
 
    return "key doesn't exist"


v1=max(nestle_products.values())
print("The top selling product from Nestle is =  ",get_key(v1,nestle_products), v1)

# Printing the top selling product from unilever with sales  figures
v2=max(unilever_products.values())
print("The top selling product from unilever is =  ",get_key(v2,unilever_products), v2)

# creating sets
Nestle_set = { "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_set ={ "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
#print(Nestle_set.union(Unilever_set))
v11={n for n in Nestle_set | Unilever_set  }
print ("this is the union between nest list and unilever list " , v11)
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
#print(Nestle_set.intersection(Unilever_set))
v22={n for n in Nestle_set &  Unilever_set }
print ("this is the  intersection between nest list and unilever list " , v22)
#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
#print (Nestle_set.difference(Unilever_set))
v33={n for n in Nestle_set - Unilever_set }
print ("this is the difrence between nest list and unilever list " , v33)

