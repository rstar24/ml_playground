# THis is the file for making the python tutorial programs 
marks = { "Maths" : 45, "Science" : 23 , "Social" : 38}
print(marks)
print(type(marks))
print(marks['Maths'])
# print(marks['Hindi'])
marks['Hindi'] = 100
print(marks['Hindi'])

set_1 = {1,2,3,4,5,}
set_1.add(6)
print(set_1.pop())
print(set_1)
# for x in set_1:
#     print(x)

a = input(str("Enter the subject "))
if(a in marks):
    print('Hindi is in the dictionary ')
    
for x in marks.values():
    print(x)
    
print(sorted(marks))