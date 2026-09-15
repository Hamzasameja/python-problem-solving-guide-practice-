a = 7
b = 3
print ("Before:",a,b)

a, b = b, a
print ("After (tuple method):",a,b)

a = 7
b = 3

temp = a
a = b
b = temp

print ("After (temp method):",a,b)