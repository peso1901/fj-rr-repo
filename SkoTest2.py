

p_Alder = {
"Peter":60,
"Helge":31,
"Challe":50
}
p_Skos = {
"Peter":50,
"Helge":46,
"Challe":10
}

alder_Listan = sorted([p_Alder["Peter"],p_Alder["Helge"],p_Alder["Challe"]])


aldst = alder_Listan[-1] #Den äldsta i listan, denna variabel använder man för att ta reda på namnet på personen i den inverterade dicten sen.
print(aldst)




#inverta detta för att få ut namnet på personen med åldern


p_Namn_Alder = {v: k for k, v in p_Alder.items()}

print(p_Namn_Alder[aldst])

p_varde_aldst = aldst
p_Namn_Aldst = p_Namn_Alder[aldst]      #Ålder och namn på den älsta personen.




#skostorleksdelen 


sko_Listan = sorted([p_Skos["Peter"],p_Skos["Helge"],p_Skos["Challe"]])

median_Sko = sko_Listan[1] #mediaskonvärdet

print(median_Sko)

p_sko_Namn = {v: k for k, v in p_Skos.items()}

p_Median_Namn = p_sko_Namn[median_Sko]

print(p_Median_Namn)  #Medianpersonens namn.






# Att göra: ta inputs och sätt dom i dicterna. Skriva ut outputs till användaren(prints()) 























"""#ta ut vilken person som är äldst
age1=ls4[0][1]
age2=ls4[1][1]
age3=ls4[2][1]
alder = max(ls4[0:1][0:2])
print(alder)"""

"""quest = input("namn, alder eller size")
print(f"Namn:{}\nÄr äldst och är {} år\nMed skostorlek {}")
print(f"Personen som har median skotorlek är {} och är ")
"""





























"""namn = str.title((input("Namn: ")))
alder = int(input("Ålder: "))
skostorlek = int(input("Skostorlek: "))
ls = [namn, alder, skostorlek]
"""



"""namn2 = str.title((input("Namn: ")))
alder2 = int(input("Ålder: "))
skostorlek2 = int(input("Skostorlek: "))
ls2 = [namn2, alde2r, skostorlek2]
namn3 = str.title((input("Namn: ")))
alder3 = int(input("Ålder: "))
skostorlek3 = int(input("Skostorlek: "))
ls3 = [namn, alder, skostorlek]"""





















"""namn1 = str(input("Namn: "))
alder1 = int(input("Ålder: "))
skostorlek1 = int(input("Skostorlek: "))
namn2 = str(input("Namn: "))
alder2 = int(input("Ålder: "))
skostorlek2 = int(input("Skostorlek: "))"""