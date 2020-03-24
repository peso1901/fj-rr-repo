X = 1
Y = 4
addresses = {"Adam": "Ormvägen 5","Bella": "Klockgatan 1","Cornelia": "Vikingagatan 3"}
cars = ["Volvo", "Opel", "BMW"]
numbers1 = {1, 2, 3, X, 6}
numbers2 = {Y, 2, 3, 4, 7}

print(addresses["Bella"])






addresses["Daniel"] = "Prinsgränd 2"
addresses["Bertil"] = "Bullerbyvägen 2"
print(addresses)
print(len(addresses))   #5

addresses["Greger"] = "Tjorvsviken 1"
test = sorted(addresses.keys())[-1]
print(addresses[test])  #5.1


addresses = {v: k for k, v in addresses.items()}
test = sorted(addresses.keys())[0]
print(addresses[test])  #5.2


print(type(cars))   #6

print(cars[X])  #7
#print(cars[Y])  #8

cars.sort()
print(cars[0])  #9

cars_2 = cars
cars_2.append("Saab")
sorted(cars_2)
print(cars + cars_2) #10

cars_3 = cars.copy()
print(cars_3)   #10.1

cars += cars
cars.sort()
cars.reverse()
print(cars) #10.2

unique_cars = cars.copy()
unique_cars = list(dict.fromkeys(unique_cars))
print(unique_cars)  #10.3

#11 finns förklarad i txt.filen

unika_nr = numbers1 | numbers2
print(unika_nr)     #12

intersection = numbers1 & numbers2
print(intersection) #13


unika_nr = numbers1 | numbers2
print(unika_nr)     #14

difference = numbers1 - numbers2
difference2 = numbers2 - numbers1
print(difference)  
print(difference2)  #15