#Multi-demensional sequences
tic_tac_toe = [['X', 'O', 'X'], [' ', 'X', ' '], ['O', 'O', 'X']]
print(tic_tac_toe[0][0], tic_tac_toe[0][1], tic_tac_toe[0][2])
print(tic_tac_toe[1][0], tic_tac_toe[1][1], tic_tac_toe[1][2])
print(tic_tac_toe[2][0], tic_tac_toe[2][1], tic_tac_toe[2][2])

list1 = [[1,2,3], [4,5,6], ["abc", "def", "ghi"]]
letter1 = list1[2][0][1]
print("\n"+letter1)
letter2 = ((list1[2])[0])[1]
print(letter2) #prints same letter as letter1
num = list1[1:3][0][2]# apply the leftmost slice/index first
print(num)

#identifying different types of outputs from expressions
tup = ([1,2,3], True, (4,5,[6]),[])
xs = ["hi", (1,),(2),[3,4,5,6],()]
print("\n"+str(xs[2])) #int
print(tup[xs[2]]) #tuple
print((xs,)) #tuple
print(tup[-1]) #list
print(xs[-tup[-2][-2]]) #string
print([tup,xs,(3,4,5)]) #list

#Nested Index loops, which is a for loop inside a for loop
zss = [[5,6,7],[8,9,10]]
for i in range(len(zss)):
	for j in range(len(zss[i])):
		print(zss[i][j])
	print("\n")

for zs in zss: #print same thing as previous code but nested value not index
	for z in zs:
		print(z)
	print("\n")
	
vals = [1,2,3,4,5,6]
characters = "Anoop"
if 4 in vals: # checking value is in the list
	print(True)
else:
	print(False)

if 9 not in vals: #checking that the value is not in the list
	print(True)
else:
	print(False)

if "oo" in characters: #can be used in strings as well
	print(True)
else:
	print(False)

print(min(characters)) #min function
print(max(vals)) #max function

#Mutable sequences we can change
list2 = [1,2,3,4]
list2[1] = 99
print("\n", list2)

list2[1:3] = [6,7,8,9]
print(list2)

#.append() , .extend() , .insert(i,x) , .pop() , .reverse(), .sort()
#id() for memory location