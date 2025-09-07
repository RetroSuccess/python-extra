import math

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print("Even")
for i in list1:
    if i % 2 == 0:
        print(i)

print("")  

print("Odd")
for j in list2:
    if j % 2 != 0:  
        print(j)
    
names = ["Jow","EMY","Timmah"]
names.append('Jimbo')
grades = [1,2,3,4]
grades[2] = len(names)
names[0] = 'EVE' + 'NT'
prog511 = names + grades

print(prog511)