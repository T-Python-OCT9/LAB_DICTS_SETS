#Create a variable
dic_Nestle= {"KitKat ": 34456432, "Nescafe  ": 14106132,"Maggi  ": 9960312,"Nido  ": 44506003}
dic_Unilever= {"Lipton  ": 23456000, "Breyers   ": 1235891,"HellManns   ": 17241412 ,"Marmite  : ": 11715324}

#for print
counter1 = 0
print("product of nestle: ")
for x,y in dic_Nestle.items():
    print(x ,":",y)
    counter1 = counter1 + 1

counter2 = 0
print("product of Unilever: ")
for z,i in dic_Unilever.items():
    print(z ,":",i )
    counter2 = counter2 + 1


#for top product
MaxSales1 = dic_Nestle.values()
print("the max is: ", max(MaxSales1))

MaxSales2 = dic_Unilever.values()
print("the max is: ", max(MaxSales2))

#most productive company
if counter1 > counter2:
    print(end=" ")
    print("Nestle is more than Unilever ")
if counter1 < counter2:
    print(end=" ")
    print("Unilever is more than Nestle ")
if  counter1 == counter2:
    print(end=" ")
    print("Nestle is eqale with Unilever ")    
       

#Using Sets
set_Nestle = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}  
set_Unilever = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print(set_Nestle.union(set_Unilever)) 
print(set_Nestle.intersection(set_Unilever)) 
print(set_Nestle.difference(set_Unilever))     
     