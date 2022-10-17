from multiprocessing import Value


Kate_Nestla = {
'34,456,432 US Dollars' : 'Kitkat',
'14,106,132 US Dollars' :'Nescafe',
 '9,960,312 US Dollars' : 'Maggi',
 '44,506,003 US Dollars' :'Nido'
}

Dalia_Unilever = {
'Lipton' : ('23,456,000 US Dollars'),
'Breyers' : ('1,235,891 US Dollars'),
 'HellManns' : ('17,241,412 US Dollars'),
 'Marmite' : ('11,715,324 US Dollars'),
}

Nestla_cuntries = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}

Unilevere_cuntries = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

Kate_Nestla_values = Kate_Nestla.values()
Dalia_Unilever_values = Dalia_Unilever.values()

print(Kate_Nestla)
print(Dalia_Unilever)

if Kate_Nestla.keys() > Dalia_Unilever.keys():
    print('Nwstla company has more products')

elif Dalia_Unilever.keys() > Kate_Nestla.keys():
    print('Unilever')

else: print('They all have the same numbers of products')

most_sold_product_Nestla = 0


Nestla_Unilever_cities = Nestla_cuntries.intersection(Unilevere_cuntries)


print('They all sell in: ',Nestla_Unilever_cities)

print('Nesla sell thier product in: ',Nestla_cuntries)

print('cities Nestle sells in',Nestla_cuntries.difference(Unilevere_cuntries),"but Unilver doens't sell in")












