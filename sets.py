
#creat dicitionary

products_sales_Nestle={ 
"KitKat" : "34,456,432",
"Nescafe" : "14,106,132",
"Maggi" : "9,960,312",
"Nido" : "44,506,003"}
products_sales_Unilever={"Lipton":"23,456,000",
"Breyers":"1,235,891",
"HellManns":"17,241,412",
"Marmite":"11,715,324"}

#print each product 

for key,value in products_sales_Nestle.items():
    print(f"the sales figures for {key} is {value}")

for key,value in products_sales_Unilever.items():
    print(f"the sales figures for {key} is {value}")


#Print the top selling product
list_products_sales_Nestle=list(products_sales_Nestle.values())
list_products_sales_Unilever=list(products_sales_Unilever.values())
map(int,list_products_sales_Nestle)
print(max(list_products_sales_Nestle))
print(max(list_products_sales_Unilever))

#companies has more products that the other company

new_list=list_products_sales_Nestle+list_products_sales_Unilever
print(max(new_list))



#print all the cities Unilever & Nestle sell their products in

nestle_sell= {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilever_sell={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
print(nestle_sell | unilever_sell)

#print the cities that both Nestle & Unilver sell in common

print(nestle_sell | unilever_sell)

#print the cities Nestle sells in , but Unilver doens't sell in

print(nestle_sell - unilever_sell)








