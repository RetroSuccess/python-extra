"""
list1 = [1,2]
list2 = [3,4]

print(list1 + list2)
print(list1*2)

grades = ["A","B","C","D"]
grades[0]

print(len(grades))

names = ["Jow","EMY","Timmah"]
names.append('Jimbo')
grades = [1,2,3,4]
grades[2] = len(names)
names[0] = 'EVE' + 'NT'
prog511 = names + grades

print(prog511)

"""
"""
# SLicing lists
grades = ["a","b","c","d"]
print(grades[-4::2])

myList = [1,2,3,4,5]

for i in myList:
    print(i,end="")
"""

list = []

for i in range(5):
    answer = int(input(f"Enter numbers {i + 1}: "))
    list.append(answer)

print(list)




