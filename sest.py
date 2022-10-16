'''# LAB_DICTS_SETS

### Kate, Dalia & Monica are work associates . They all work at a consultancy company.

## Kate has the products sales of Nestle :

##### KitKat : 34,456,432 US Dollars
##### Nescafe : 14,106,132 US Dollars
##### Maggi : 9,960,312 US Dollars
##### Nido : 44,506,003 US Dollars

Unilever_Dict={"Lipton":"23,456,000 US Dollars","Breyers":"1,235,891 US Dollars","HellManns":"17,241,412 US Dollars","Marmite":"11,715,324 US Dollars"}

## Dalia has the products sales of Unilever :

##### Lipton : 23,456,000 US Dollars
##### Breyers : 1,235,891 US Dollars
##### HellManns : 17,241,412 US Dollars
##### Marmite : 11,715,324 US Dollars
      

## Monica has 2 tables containing the countries in which Unilever and Nestle sell the products:
##### Nestle : "Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"
##### Unilever : "Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"


## Using what you've learned during . Please do the following :
- Create a variable to hold the values of Nestle products (use a dicitionary)
- Create a variable to hold the values of Unilever products (Use a dictionary)
- Print each product sold by Unilever and the sales figures / numbers  for that product.
- Print each product sold by Nestle and the sales figures / numbers  for that product.
- Print which of the companies has more products that the other company.
- Print the top selling product from Nestle with sales figures.
- Print the top selling product from Unilever with sales figures.

- Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.




'''
from multiprocessing.sharedctypes import Value

Nestle_set={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"} 
Unilever_set={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"} 
nestle_Dict={"kitKat":"34456432","Nescafe":"14106132","Maggi":"9960312","NIDO":"44506003"}
Unilever_Dict={"Lipton":"23456000","Breyers":"1235891","HellManns":"17241412","Marmite":"11715324"}


print(f"\n the prodects are sold by Nestle and there sales numbers are \n")
for x,y in nestle_Dict.items():
    print(x,y+" US Dollars\n")
print(f"\n the prodects are sold by Unilever and there sales numbers are \n")
for x,y in Unilever_Dict.items():
    print(x,y+" US Dollars\n")

#result :int  = 0

nestle_total=sum(int (i) for i in nestle_Dict.values())
Unilever_total=sum(int (i) for i in Unilever_Dict.values())
#print(nestle_total)  
#print(Unilever_total) 
if nestle_total>=nestle_total:
    print("Nestle Company has more products sold than Unilever company")
else:
    print("Unilever Company has more products sold than Nestle company")

print("the top selling Product in Nestle company is \n",max(int (i) for i in nestle_Dict.values()))
print("the top selling Product in Unilever company is \n",max(int (i) for i in Unilever_Dict.values()))

for i in nestle_Dict:
   if max(int(i) for i in nestle_Dict.values()):
        print (nestle_Dict.keys())



print("all the cities that Unilever & Nestle sell their products are\n",Nestle_set.union(Unilever_set))
print("the common cities that Unilever & Nestle sell their products are\n",Nestle_set.intersection(Unilever_set))
print("the cities Nestle sells in , but Unilver doens't sell in\n",Nestle_set.difference(Unilever_set))

#print(sum(nestle_Dict.values()))



#print(result)