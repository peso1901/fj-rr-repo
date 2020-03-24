#Samla inputs till dicterna.
name1 = str.title((input("Namn: ")))
alder1 = int(input("Ålder: "))
skostorlek1 = int(input("Skostorlek: "))
name2 = str.title((input("Namn: ")))
alder2 = int(input("Ålder: "))
skostorlek2 = int(input("Skostorlek: "))
name3 = str.title((input("Namn: ")))
alder3 = int(input("Ålder: "))
skostorlek3 = int(input("Skostorlek: "))


#Skapar två dicter, p_alder  Namn -> ålder och p_Skos sparar Namn -> Skostorlek.
p_Alder = {name1:alder1, name2:alder2, name3:alder3}
p_Skos = {name1:skostorlek1, name2:skostorlek2, name3:skostorlek3}

#Skapar en lista utav ålderdicten, för att sedan ta ur väldet på den som är äldst.
alder_Listan = sorted([p_Alder[name1],p_Alder[name2],p_Alder[name3]])                                                            
aldst = alder_Listan[-1] #Den äldsta i listan, denna variabel använder man för att ta reda på namnet på personen i den inverterade dicten sen.

#Denna inverterar ålder dicten. Så att åldern är keyn och namnet blir value.
p_Namn_Alder = {v: k for k, v in p_Alder.items()}



#skapar en variabel som får ut namnet på den som är äldst. Och meddelar det till användaren.
p_Namn_Aldst = p_Namn_Alder[aldst]    
print(f"Den äldsta personen är \"{p_Namn_Aldst}\".")




#Skapar en lista utav p_Skos, för att sedan sortera den och efter det kunna ta ut vilken person som har medianskovärdet.
sko_Listan = sorted([p_Skos[name1],p_Skos[name2],p_Skos[name3]])
median_Sko = sko_Listan[1] #mediaskonvärdet

#Skapar en "inverterad" dict av p_Skos dicten. För att kunna söka på skostorleken och få ut tillhörande namn. 
p_sko_Namn = {v: k for k, v in p_Skos.items()}
p_Median_Namn = p_sko_Namn[median_Sko]  # får ut namnet på personen med medianskovärdet.
print(f"Personen \"{p_Median_Namn}\" har medianskostorleken.")


#Följande tar in input och skickar ut all information till inputen.
soek_variable = input("Fråga efter namn, age eller size och dess sökaltenativ: ")                                                       
xer = soek_variable.rsplit(" ")         #delar upp inputen i 2 delar, för att kunna användas till att få fram informationen.

#if-satsen som hittar informationen.
if xer[0] == "age":
        soek = int(xer[1])      #typomvandlar till en int för att du ska kunna änvada den i 2 dicter.
        namn = p_Namn_Alder[soek] 
        shoe = p_Skos[namn]
        print(f"Namn: {namn}\nSkostorlek: {shoe}\nÅlder: {xer[1]}")
elif xer[0] == "namn":
        soek = str(xer[1])      #typomvandlar till en sträng för att du ska kunna änvada den i 2 dicter.
        shoe = p_Skos[soek]
        age = p_Alder[soek]
        print(f"Namn: {xer[1]}\nSkostorlek: {shoe}\nÅlder: {age}")
elif xer[0] == "size":
        soek = int(xer[1])
        namn = p_sko_Namn[soek]
        age = p_Alder[namn]
        print(f"Namn: {namn}\nSkostorlek: {xer[1]}\nÅlder: {age}")      
else:
        print("Fel input.")




