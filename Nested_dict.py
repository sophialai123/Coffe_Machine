
#Access elements of a Nested Dictionary
people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)

print(people[1]["name"])
print(people[1]["age"])
print(people[1]["sex"])

#Add element to a Nested Dictionary
#Example 3: How to change or add elements in a nested dictionary?

people[3] = {}
people[3]["name"] = "Luna"
people[3]["age"] = "34"
people[3]["sex"] = "Female"
people[3]["married"] = "No"

print(people)

#Example 4: Add another dictionary to the nested dictionary

people[4] = {'name': 'Peter', 'age': '29', 'sex': 'Male',"married": "Yes"}
print(people[4])
print(people)

# Delete elements from a Nested Dictionary
del people [3]["married"]
del people[4]["married"]
print(people[3])
print(people[4])

#How to delete dictionary from a nested dictionary?
del people [3], people[4]
print(people)

#Iterating Through a Nested Dictionary
people = {1: {'Name': 'John', 'Age': '27', 'Sex': 'Male'},
          2: {'Name': 'Marie', 'Age': '22', 'Sex': 'Female'}}

for p_id , p_info in people.items(): # p_id is the key , p_info is the value
    print("\nperson ID:", p_id) # print key only
    for key in p_info: # the key in nested dict, p_info is the nested dict
        print(key + ":", p_info [key]) # the key of nested dict, + the value of nested dict



#https://www.w3resource.com/python-exercises/dictionary/
#Python Data Types: Dictionary - Exercises, Practice, Solution
#Add a key to a dictionary
sam_dict = {0:10,1:20}
sam_dict [2] = 30
print(sam_dict)


sam_dict.update({4:35}) # use update() to add a key to a dictionary
print(sam_dict)

#Write a Python script to concatenate following dictionaries to create a new one
new_dict = {}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
for d in (dic1,dic2,dic3): # use for loop
    print(d)
    new_dict.update(d)
print(new_dict)


# Check whether a given key already exists in a dictionary
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
def is_key_present(x):
    if x in d:
        print(f"{x} is present in the dictionary.")
    else:
        print(f"{x} is not present in the dictionary.")

is_key_present(5)
is_key_present(9)
#Write a Python program to iterate over dictionaries using for loops.

for key,value in d.items():
    #print(f"{key} : {d[key]}")
    print(key, ":" ,value) # two are the same output

#Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x)
out_put = {}
for x in range(1,6):
    out_put [x] = x*x
print(out_put)

#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys
dict_square = {}
for y in range(1,16):
    dict_square[y] = y**2 # square
print(dict_square)

#Merge two Python dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
d.update(d2)
print(d)

# Write a Python program to iterate over dictionaries using for loops
dicts = {'a': 100, 'b': 200, 'x': 300, 'y': 400}
for key,value in dicts.items():
    print(f"{key}: {value}")

#Sum all the items in a dictionary
print(sum(dicts.values()))

#Multiply all numbers in the list
def multiply(my_list):
    result = 1
    for x in my_list:
        result *= x
    return result
print(multiply([3, 2, 5, 4]))

#Multiply all numbers in the dictionary:
dicts = {'a': 3, 'b': 2, 'x': 3, 'y': 4}
result1 = 1
for x in dicts:
    result1 *= dicts[x]
print(result1)






