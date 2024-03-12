#Demonstration of a tuple 
a = (x for x in range(100) if x % 2 == 0)

for i in a:
    print(i)

print(a)
