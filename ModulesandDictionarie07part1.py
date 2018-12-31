#import moduleName
#from moduleName import thing
#from moduleName import (thing1, thing2, thing3)
#from moduleName import*


#Dictonarys
GradesperPerson = {"Anoop":98, "Harsh":92, "Anil":90}
GradesperPerson["Rachna"] = 88 #creates a new entity at the end of dictonary
print(GradesperPerson)
print(GradesperPerson["Harsh"]) #how to access dictory value

a = GradesperPerson.get("Anoop")
print(a)
b = len(GradesperPerson)
print(b)
del GradesperPerson["Rachna"]
print(GradesperPerson)
c = GradesperPerson.keys()
print(c)
d = GradesperPerson.values()
print(d)
e = GradesperPerson.items()
print(e)
GradesperPerson.pop("Harsh")
print(GradesperPerson)

GradesperPerson2 = {"Arnav":90, "Ansh":99}
GradesperPerson.update(GradesperPerson2)
print(str(GradesperPerson) +"\n")

#Dictonary Iteration
print("BY KEYS!!!!:")
for name in GradesperPerson:
	print(name, GradesperPerson[name])

print("\nBY VALUES!!!:")
for grade in GradesperPerson.values():
	print(grade)

print("\nBY ITEMS!!!:")
for (name,grade) in GradesperPerson.items():
	print(name,grade)