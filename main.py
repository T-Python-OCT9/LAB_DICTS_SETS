Kate_nestle={'KitKat' :34456432 ,'Nescafe' : 14106132,'Maggi' : 9960312,'Nido' : 44506003}
Dalia_unilever={'Lipton' :23456000,'Breyers' : 1235891,'HellManns' : 17241412,'Marmite' : 11715324}

print('Kate_nestle')
for k1,v1 in Kate_nestle.items():
    print(f"{k1} : {v1}US Dollars")
#print(max(Kate_nestle))
#for Key in Kate_nestle:
 #   print(Kate_nestle[Key])

print('Dalia_unilever')
for k2,v2 in Dalia_unilever.items():
    print(f"{k2} : {v2}US Dollars")

if len(Kate_nestle) > len(Dalia_unilever):
    print("Nestle has more products")
elif len(Dalia_unilever) > len(Kate_nestle):
    print("Unilver has more products")
else:
    print("Unilver & Nestle has the same products count")

nestle_most_sold_product_figure = 0
nestle_most_sold_product = None

for key, value in Kate_nestle.items():
    if value > nestle_most_sold_product_figure:
        nestle_most_sold_product_figure = value
        nestle_most_sold_product = key

print("The Most sold product in Nestle:")
print(f"{nestle_most_sold_product} {nestle_most_sold_product_figure} US Dollars")


print("The most sold product in Unilever:")
unilver_most_sold_product = max(Dalia_unilever)
unilver_most_sold_product_figure = Dalia_unilever[unilver_most_sold_product]
print(f"{unilver_most_sold_product} {unilver_most_sold_product_figure} US Dollars")

print("The most sold product in Unilever:")
unilver_most_sold_product = max(Dalia_unilever)
unilver_most_sold_product_figure = Dalia_unilever[unilver_most_sold_product]
print(f"{unilver_most_sold_product} {unilver_most_sold_product_figure} US Dollars")
print("-"*10)


Nestle_countries={"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
Unileve_countries={"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}
#print(Nestle.intersection(Unileve))
#print(Nestle | Unileve)
#print(Nestle - Unileve)
print("The countries where Unilver & Nestle sell product:")
nestle_unilver_countries_set = Nestle_countries | Unileve_countries
for country in nestle_unilver_countries_set:
    print(f"Country: {country}")

print("The countries where Unilver & Nestle both sell product in:")
nestle_unilver_countries_inter_set = Unileve_countries & Nestle_countries

for country in nestle_unilver_countries_inter_set:
    print(f"Country: {country}")



print("The countries where  Nestle selld product in but not Unilver:")
nestle_unilver_countries_diff_set = Nestle_countries - Unileve_countries

for country in nestle_unilver_countries_diff_set:
    print(f"Country: {country}")

