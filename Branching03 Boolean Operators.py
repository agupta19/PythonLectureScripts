#Boolean operators include: and, or, not
#Relationship operatiors include: <,<=,>,>=,!=(inequality check)
#Use == not just one =

x=2
y=4
b=True

if (x<y) and b:
	print("This boolean operator works")

if True or True and False:
	print("This boolean operator works as well")

if not(b):
	print("Result is True")
else:
	print("Result is False")

num = 10 #Change this around to affect result 
if num < 10:
	print("This number is too small")
else:
	if num == 10:
		print("This is the number!")
	else:
		print("This number is too big!")

#Flow charts help with if, elif, else statements 

guess = 42 #Change these numbers to affect the code
secret = 42
if guess > secret:
	print("too big")
elif guess < secret:
	print("too small")
else:
	print("correct!")
