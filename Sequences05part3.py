# multiple ways to access same spot of memory is Aliasing!
xs = [1,2,3]
ys = [4,5,6]
both = [xs,ys]
xs[1] = 7
print(xs)
print(both, "\n")
ys = [8,9]
print(ys)
print(both #you have to update both again to update ys

#Re-assigning: can be different memory location. xs = newExpression
#Updating: changes the content but same locaiton. xs[0] = newval