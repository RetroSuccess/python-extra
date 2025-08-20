"""
Exercise 1: Perform dictionary operations

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
Perform following operations on given dictionary
1. Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary
and print the updated dictionary.
2. Modify Value: Change the value of the age key to 40 in the dictionary and print the updated
dictionary.
3. Access Key: Print the value associated with the city key.
"""

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
my_dict.update({'profession': 'Doctor'})
print(my_dict)

my_dict['age'] = 40
print(my_dict)

print(my_dict['city'])


"""
Exercise 2: Perform dictionary operations
Given:
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
Perform following operations on given dictionary
1. Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
2. Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
3. Check if Key Exists in the dictionary
"""

my_dict.pop('profession')
print(my_dict)

print("Values:", list(my_dict.values()))

# Check if a key exists
if 'city' in my_dict:
    print("Key 'city' exists!")
else:
    print("Key 'city' does not exist.")


"""
Exercise 3: Dictionary from Lists
Write a Python program to convert two Python lists into a dictionary where elements from the first
list become keys and elements from the second list become values.
"""
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

mix = dict(zip(keys, values))
print(mix)


"""
Exercise 4: Clear Dictionary
Clear all key-value pairs from a given dictionary and print it.
Given:
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
"""
my_dict.clear()
print(my_dict)

