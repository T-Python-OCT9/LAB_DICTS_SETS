nestle = {'KitKat': 34456432, 'Nescafe': 14106132, 'Maggi': 9960312, 'Nido': 44506003}
unilever = {'Lipton': 23456000, 'Breyers': 1235891, 'HallManns': 17241412, 'Marmite': 11715324}

nestle_countries_set = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
unilver_countries_set = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("Products sold by Nestle:")
for key, value in nestle.items():
        print(f"{key}: {value} US Dollars")

print("*" * 10)
print("Products sold by Unilever:")
for key, value in unilever.items():
        print(f"{key}: {value} US Dollars")

if len(nestle) > len(unilever):
        print("Nestle has more products")
elif len(unilever) > len(nestle):
        print("Unilver has more products")
else:
        print("Unilver & Nestle has the same products count")

nestle_most_sold_product_figure = 0
nestle_most_sold_product = None

for key, value in nestle.items():
        if value > nestle_most_sold_product_figure:
            nestle_most_sold_product_figure = value
            nestle_most_sold_product = key

print("The Most sold product in Nestle:")
print(f"{nestle_most_sold_product} {nestle_most_sold_product_figure} US Dollars")

print("The most sold product in Unilever:")
unilver_most_sold_product = max(unilever)
unilver_most_sold_product_figure = unilever[unilver_most_sold_product]
print(f"{unilver_most_sold_product} {unilver_most_sold_product_figure} US Dollars")

print("-" * 10)
print("The countries where Unilver & Nestle sell product:")
nestle_unilver_countries_set = unilver_countries_set | nestle_countries_set

for country in nestle_unilver_countries_set:
        print(f"Country: {country}")

        print("The countries where Unilver & Nestle both sell product in:")
        nestle_unilver_countries_inter_set = unilver_countries_set & nestle_countries_set

        for country in nestle_unilver_countries_inter_set:
            print(f"Country: {country}")

        print("The countries where  Nestle selld product in but not Unilver:")
        nestle_unilver_countries_diff_set = nestle_countries_set - unilver_countries_set

        for country in nestle_unilver_countries_diff_set:
            print(f"Country: {country}")
