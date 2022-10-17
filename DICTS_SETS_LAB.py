nestle = {'KitKat' : 34456432,
'Nescafe' : 14106132,
'Maggi' : 9960312,
'Nido' : 44506003}

unilever = {'Lipton' : 23456000,
'Breyers' : 1235891,
'HellManns' : 17241412,
'Marmite' : 11715324 }

unilever_cities = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
nestle_citite = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}


def unilever_data(): 
    print("--Products Sold By Nestle--")
    for product , sales in nestle.items():
        print(f'The Product Is {product}\nSALES: {sales} US Dollars')

def nestle_data():
    print("--Products Sold By Unilever--")
    for product , sales in unilever.items():
        print(f'The Product Is {product}\nSALES: {sales} US Dollars')
    

def more_product():
    print("--The Company that Has More Products--")
    if len(nestle.keys()) > len(unilever.keys()):
        print("Nestle Has More Products Than Unilever!")
    elif  len(nestle.keys()) < len(unilever.keys()):
        print("Unilever Has More Products Than Nestle!")
    else:
        print("They Are Equal!")


def top_silling_for_nestle():
    max_product_price = 0
    max_product_name = ""
    for product , sales in nestle.items():
        if sales > max_product_price:
            max_product_price = sales
            max_product_name = product
    print(f"The Top Saling Product For Nestle is: {max_product_name}\nSALES:{max_product_price}")

def top_silling_for_unilever():
    max_product_price = 0
    max_product_name = ""
    for product , sales in unilever.items():
        if sales > max_product_price:
            max_product_price = sales
            max_product_name = product
    print(f"The Top Saling Product For Nestle is: {max_product_name}\nSALES:{max_product_price}")


nestle_data()
unilever_data()
more_product()
top_silling_for_nestle()
top_silling_for_unilever()

print(unilever_cities | nestle_citite)  # print all the cities Unilever & Nestle sell their products in

print(unilever_cities & nestle_citite)  # print the cities that both Nestle & Unilver sell in common.

print(nestle_citite - unilever_cities) # print the cities Nestle sells in , but Unilver doens't sell in.





    


        
    







