Nestle = {"KitKat":"34,456,432 US Dollars","Nescafe":"14,106,132 US Dollars", "Maggi" :"9,960,312 US Dollars" ,"Nido":"44,506,003 US Dollars" }
Unilever ={"Lipton":"23,456,000 US Dollars","Breyers":"1,235,891 US Dollars","HellManns":"17,241,412 US Dollars","Marmite":"11,715,324 US Dollars"}
NestleC = {"Saudi Arabia", "Oman", "Kuwait", "Egypt", "Jordan", "Sudan"}
UnileverC = {"Saudi Arabia", "Kuwait", "Iraq", "Morocco", "Yemen", "United Emirates"}

print("Unilever")
for k2, v2 in Unilever.items():
    print(f"Product name is: {k2}  The price is: {v2}")


print("Nestle")
for k1, v1 in Nestle.items():
    print(f"Product name is: {k1}  The price is: {v1}")

if len(Nestle) ==len(Unilever):
    print("The product number equal each other...")
if len(Nestle) > len(Unilever):
    print("The product number of Nestle more than Unilever...")
if len(Nestle) < len(Unilever):
    print("The product number of Unilever more than Nestle...")

#Nestle Top

listN = []
for i in Nestle:
    s = Nestle[i].split(" ")
    s2 = s[0]
    resultN = int(s2.replace(',', ''))
    listN.append(resultN)


for key,val in Nestle.items():
    ii = Nestle[key].split(" ")
    ii1 = ii[0]
    resultN2 = int(ii1.replace(',', ''))
   
    if resultN2 == max(listN):
        print("The top selling product from Nestle is: ", key ,"  With salary : ", val)

#Unilever Top


listU = []
for i in Unilever:
    splitU = Unilever[i].split(" ")
    splitU1 = splitU[0]
    resultU = int(splitU1.replace(',', ''))
    listU.append(resultU)


for key,val in Unilever.items():
    splitU = Unilever[key].split(" ")
    splitU1 = splitU[0]
    resultU = int(splitU1.replace(',', ''))
   
    if resultU == max(listU):
        print("The top selling product from Unilever is: ", key ,"  With salary : ", val)

print("All the cities Unilever & Nestle",NestleC|UnileverC)
print("The cities that both Nestle & Unilver sell in common",NestleC&UnileverC)
print("the cities Nestle sells in , but Unilver doens't sell in",NestleC-UnileverC)
