def max_3 (a,b,c):
	if a >=b and a >=c:
		return a #returning immedietly exits the function 
	if b >=c:
		return b
	return c 

x = max_3(6,7,8) #how to call a function
print (x)


#Using One fucntion to call another
def average(xs):
	sum = 0
	for x in xs:
		sum+= x
	return float(sum) / len(xs)

def main():
	my_list = [20,24,28]
	avg = average(my_list)
	print("Average = "+str(avg))
	#If we reach the enf of a function with no return statement, it returns None
main() #calling main function


def add_two_numbers(p1=5, p2=3): #This code has defult parameters if none are given
	return (p1+p2)

def main2():
	print(add_two_numbers())
	print(add_two_numbers(45))
	print(add_two_numbers(45,55))

main2()
