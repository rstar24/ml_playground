# To print the table of a number
a = int(input("Enter a number :"))

for i in range(11):
    if(i == 0):
        continue
    print("{} x {} = {}".format(i,a,i*a))