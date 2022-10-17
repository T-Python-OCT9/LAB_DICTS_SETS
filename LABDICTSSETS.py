'''## Using what you've learned during . Please do the following :
-++ Create a variable to hold the values of Nestle products (use a dicitionary) done
- ++Create a variable to hold the values of Unilever products (Use a dictionary) DONE 
- ++Print each product sold by Unilever and the sales figures / numbers  for that product.
+++Print each product sold by Nestle and the sales figures / numbers  for that product.
- ++ Print which of the companies has more products that the other company.
- === Print the top selling product from Nestle with sales figures.
-=== Print the top selling product from Unilever with sales figures.
- +++Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
- Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
- Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
'''

#Create a variable to hold the values of Nestle products (use a dicitionary)
NestleCountries= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

#Create a variable to hold the values of Unilever products (Use a dictionary)
UnileverCountries={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


#Print each product sold by Unilever and the sales figures / numbers  for that product.
# i can us _ for , for the big num 
Unilever_sales = { "Lipton" : 23456000 , "Breyers ": 1235891
 , "HellManns" : 17241412
 ,"Marmite" : 11715324}

for key , value in Unilever_sales.items():
    print(f" Unilever product :  {key} ,  sales: {value} US Dollars ")


print( )
# Print each product sold by Nestle and the sales figures / numbers  for that product.

Nestle_sales ={ " KitKat" : 34456432, "Nescafe" : 14106132
 , "Maggi ": 9960312 
 ,"Nido" :  44506003}

for key , value in Nestle_sales.items():
    print(f" Nestle product:  {key} ,  sales: {value} US Dollars ")

#Print which of the companies has more products that the other company.



'''
for value in Nestle_sales.values():
    sum1=sum(list( Nestle_sales.values()))
   
print(sum1)

for value in Unilever_sales.values():
    sum2=sum(list( Unilever_sales.values()))   

print(sum2)


if sum1>sum2 :
    print( "the companies has more products is Nestle : " , sum1)
else:
 print( "the companies has more products is Unilever: " , sum2) 
'''

#Print the top selling product from Nestle with sales figures.
'''
top_selling = {"top ": 00 }

for  value in Nestle_sales :
    if value > top_selling.values():
        print("hiiii")
'''
print( "the top selling product from Nestle is : " , max( Nestle_sales) )

#Print the top selling product from Unilever with sales figures

print( "the top selling product from Unilever is : " , max(Unilever_sales))

print(  )
#Using Sets & a loop, print all the cities Unilever & Nestle sell their products in.
print( " all the cities Unilever & Nestle sell ")
all_cities = UnileverCountries| NestleCountries
#print( " all the cities Unilever & Nestle sell ", UnileverCountries| NestleCountries)
for C in all_cities :
    print(f" cities: {C}") 
print(  )
#Using Sets & a loop, print the cities that both Nestle & Unilver sell in common.
print( " the cities that both Nestle & Unilver sell in ")
all_cities2 = UnileverCountries & NestleCountries
for C2 in all_cities2 :
    print(f" cities: {C2}") 
print(  )

#Using Sets & a loop, print the cities Nestle sells in , but Unilver doens't sell in.
print( " the cities Nestle sells in , but Unilver doens't sell ")
all_cities3 =  NestleCountries - UnileverCountries 
for C3 in all_cities3 :
    print(f" cities: {C3}")  
print(  )



