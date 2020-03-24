


name1 = str.title((input("Namn: ")))
alder1 = int(input("Ålder: "))
skostorlek1 = int(input("Skostorlek: "))
name2 = str.title((input("Namn: ")))
alder2 = int(input("Ålder: "))
skostorlek2 = int(input("Skostorlek: "))
name3 = str.title((input("Namn: ")))
alder3 = int(input("Ålder: "))
skostorlek3 = int(input("Skostorlek: "))



p_Alder = {name1:alder1, name2:alder2, name3:alder3}
p_Skos = {name1:skostorlek1, name2:skostorlek2, name3:skostorlek3}

alder_Listan = sorted([p_Alder[name1],p_Alder[name2],p_Alder[name3]])                                                               #([p_Alder["Peter"],p_Alder["Helge"],p_Alder["Challe"]])


aldst = alder_Listan[-1] #Den äldsta i listan, denna variabel använder man för att ta reda på namnet på personen i den inverterade dicten sen.




#inverta detta för att få ut namnet på personen med åldern


p_Namn_Alder = {v: k for k, v in p_Alder.items()}



p_varde_aldst = aldst
p_Namn_Aldst = p_Namn_Alder[aldst]      #Ålder och namn på den älsta personen.

print(f"Den äldsta personen är {p_Namn_Aldst}")


#skostorleksdelen 


sko_Listan = sorted([p_Skos[name1],p_Skos[name2],p_Skos[name3]])

median_Sko = sko_Listan[1] #mediaskonvärdet

p_sko_Namn = {v: k for k, v in p_Skos.items()}

p_Median_Namn = p_sko_Namn[median_Sko]

print(f"Personen \"{p_Median_Namn}\" har mellan storleken.")  #Medianpersonens namn.






# Att göra: ta inputs och sätt dom i dicterna. Skriva ut outputs till användaren(prints()) 

soek_variable = input("Fråga efter namn, age eller size och ett sökaltenativ: ")                                                        #   "namn Challe"
xer = soek_variable.rsplit(" ")
print(p_Namn_Alder)

if xer[0] == "age":
        soek = int(xer[1])
        namn = p_Namn_Alder[soek] 
        shoe = p_Skos[namn]
        
        print(f"Namn: {namn}\nSkostorlek: {shoe}\nÅlder: {xer[1]}")
elif xer[0] == "namn":
        soek = str(xer[1])
        shoe = p_Skos[soek]
        age = p_Alder[soek]
        print(f"Namn: {xer[1]}\nSkostorlek: {shoe}\nÅlder: {age}")
elif xer[0] == "size":
        soek = int(xer[1])
        namn = p_sko_Namn[soek]
        age = p_Alder[namn]
        print(f"Namn: {namn}\nSkostorlek: {xer[1]}\nÅlder: {age}")              #Löser att skriva ut förfrågningar efter man har skrivit in alla värden. DOCK MED IFSATS.





