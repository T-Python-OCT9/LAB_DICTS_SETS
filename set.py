from multiprocessing import Value
from re import X


Nestle_products = {"KitKat" : 34_456_432,
                   "Nescafe" : 14_106_132,
                   "Maggi" : 9_960_312,
                   "Nido" : 44_506_003 }

Unilever_products = {"Lipton" : 23_456_000,
                   "Breyers" : 1_235_891,
                   "HellManns" : 17_241_412,
                   "Marmite" : 11_715_324 }



Nestle_countries_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unilever_countries_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

for key, Value in Nestle_products.items():
    print(f"{key}:{Value} Us dollares")
print("-"*10)
for key, Value in Unilever_products.items():
    print(f"{key}:{Value} Us dollares")
print("-"*10)
if len(Nestle_products) > len(Unilever_products):
    print("Nestle has more products")
elif len(Unilever_products) > len(Nestle_products):
    print("Unilever has more products")
else:
    print("Unilver & Nestle has the same products count")
print("-"*10)

nestle_most_sold_product_figure = None
nestle_most_sold_product = None

nestle_most_sold_product_figure = max(Nestle_products)
nestle_most_sold_product = Nestle_products[nestle_most_sold_product_figure]
print(f"{nestle_most_sold_product_figure} {nestle_most_sold_product}")
print("-"*10)
Unilever_most_sold_product_figure = None
Unilever_most_sold_product = None
Unilever_most_sold_product_figure = max(Unilever_products)
Unilever_most_sold_product = Unilever_products[Unilever_most_sold_product_figure]
print(f"{Unilever_most_sold_product_figure} {Unilever_most_sold_product}")
print("-"*10)


Nestle_Unilever_union_set = Nestle_countries_set.union(Unilever_countries_set)
for i in Nestle_Unilever_union_set:
    print(f"Country: {i}")
print("-"*10)

Nestle_Unilever_intersection_set = Nestle_countries_set.intersection(Unilever_countries_set)
for i in Nestle_Unilever_intersection_set:
    print(f"Country: {i}")
print("-"*10)

Nestle_Unilever_difference_set = Nestle_countries_set.difference(Unilever_countries_set)
for i in Nestle_Unilever_difference_set:
    print(f"Country: {i}")

