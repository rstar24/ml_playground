a = str(input("Enter a string :"))

# TO remverse a string
for i in range(len(a)+1): 
    if(i <=0 ):
        continue
    print(a[-i])