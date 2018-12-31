#Augmented Assignments
#	These are shortcuts for operators
x = 10
x+= 5

x//=5
print("This is x:",x)

#Strings
#	Use quotes to make a string
#	Escape Sequences with \n or \t
y = "ice\n" + "cream\t" + "please"
print ("This is y:",y)

#Conversions
#	Using int, float, str
z = int(2.3)
zz = float("3.55")
zzz = str(4-1)

print("I have " + zzz + " apples.")


#returns type of the obejct (int or str)
type(3)
type("hello")

#Multiline statement example, has to end in \
a = 5+\
4+\
4
print(a)