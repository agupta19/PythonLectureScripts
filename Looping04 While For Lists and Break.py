#Adds x to itself when x is still lower than 100
x = 10
while x<40:
	x+=x
	print(x)

#While-Loop example for guessing a password
password = "Mason"
while password!= "Mason":
	print("Thats not the password, try again!")
	password = input("next guess: ")
print("Thats the password! Congrats!")


n = 2
while n>0:
	print(n)
	n = n-1
print("all done")

#Lists and how to create/modify them
x1 = ["Anoop", "Gupta"]
print(x1)
x1[0] = "Harsh"
print(x1[0])
print(x1)

#Generates pattern of numbers (Start,Stop,Step)
x2 = list(range(0,10,3))
x3 = list(range(10)) #Only stop with step 1 and start at 0, stops at 9
x4 = list(range(6,3,-1))
print(x2)
print(x3)
print(x4)

#For loop example1
initals = "GMU"
for letter in initals:
	print(letter)

#For loop example2
for num in range(5,0,-1):
	print(str(num)+"...")
print("LIFT OFF!!!!")

#definite loops use for, if its indefinite, use while
#break is used to exit loop, continute is used to go to next iteration