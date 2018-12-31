#A sequence is an ordered group of values (strings lists and tuples) 
#We can access each spot in a sequence with its index number
# Strings and Tuples are immutable which cant be changed
#Lists however, care mutable which can be changed
#Tuples with one entity need a comma

msg = "index"
print(msg[0]+"<<<first letter")
print(msg[-1]+"<<<last letter")

nums = [10, 11, 8, 22]
print(str(nums[-1])+"<<<last number")
print(str(nums[-4])+"<<<first number")
print(str(len(nums))+" is the length of the sequence") #checks the length of the sequence

#Value and Index For loops
Family_Names = ["Anoop", "Harsh", "Rachna", "Anil\n"]
for names in Family_Names:
	print(names)

for i in [0,1,2,3]:
	print(Family_Names[i])

for i in range(len(Family_Names)):
	print(Family_Names[i])

#Indexing in other orders
values = [11,12,13,14,15,16,17,18]
for i in range(0,len(values),2):
	print(values[i])

print("\n")

for i in range(len(values)-1,-1,-1):
	print(values[i])

#Modifying and Bulding Lists
xs = [1,-2,3,-4,-5,100,150,-30,123]
for i in range(len(xs)):
	if xs[i]<0:
		xs[i] = -xs[i]
	elif xs[i]>50:
		xs[i] = 50
print(xs)

emptylist = []
for i in range(20):
	if i%3==0 or i%5==0:
		emptylist.append(i) #adds to a list in the loop
print(emptylist)

#Slicing to grab a sub-sequence, [start:stop] or [start:stop:step]
#Similar to the range() function but with colons
words = "Hello there"
words2 = words[3:9]
words3 = words[0:10:3]
words4 = words[::-1] #reverse string
words5 = words[0:10:-1] #empty string
words6 = words[:]

print(words2)
print(words3)
print(words4)
print(words5)
print(words6)