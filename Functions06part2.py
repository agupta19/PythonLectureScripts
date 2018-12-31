def change_me (xs, i):
	xs[i] += 100
	print(xs)

def main():
	nums = [3,5,7]
	change_me(nums,2)
	print(nums)

	data = [2,4,6]
	change_me(data[:],2) #sends a copy but not the actual list
	print(data)
main()




x = 10 #global value

def f1(): 
	x = 20 #local variable 
	print("in f1, x =", x)

def f2():
	global x #changes the global value
	x = 20
	print("in f2, x = ", x)

def main2():
	print("initial x = ",x)
	f1()
	print("after f1, x = ",x)
	f2()
	print("after f2, x = ",x)

main2()