S = []
M = []
L = []


bekert= float(input("Adja meg az értéket: "))

while bekert !=0:
    if bekert >0 and bekert <=5:
        S.append(bekert)
    elif bekert >5 and bekert <=15:
        M.append(bekert)
    elif bekert >15 and bekert <=30:
        L.append(bekert)
    else:
        print("Nem értelmezhető")

    bekert= float(input("Adja meg az értéket: "))

print(len(S))
print()
print(len(M))
print()
print(len(L))