# https://www.w3resource.com/python-exercises/python-functions-exercises.php
# practice function


#Write a Python program to reverse a string
def string():
    reverse_string = "1234abcd" [::-1]
    return reverse_string
print(string())

#Sample Solution-2:
def reverse(itr):
  return itr[::-1]

str1 = '1234abcd'
print("Original string:",str1)
print("Reverse strig:",reverse('1234abcd'))
str1 = 'reverse'
print("\nOriginal string:",str1)
print("Reverse strig:",reverse(str1))


#The factorial formula is: n! = n*(n -1)!
#A factorial is a function in mathematics with the symbol (!) that multiplies a number (n) by every number that precedes it.
# eg: 4! = 4 x 3 x 2 x 1 = 24.

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(int(input("A number: "))))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def check_cases():
    count1 = 0
    count2 = 0
    sample_string = "The quick Brown Fox"
    for string in sample_string:
        if (string.isupper()) == True:
            count1 += 1

        elif (string.islower()) == True:
            count2+= 1
        else:
            pass
    print(f"No. of Upper case characters : {count1}")
    print(f"No. of Lower case characters : {count2}")

check_cases()

# Sameple Solution
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("No. of Upper case characters : ", d["UPPER_CASE"])
    print ("No. of Lower case Characters : ", d["LOWER_CASE"])

string_test('The quick Brown Fox')


#Write a Python function that takes a list and returns a new list with unique elements of the first list.
def unique_list():
    unique_list = []
    my_list = [1, 2, 3, 3, 3, 3, 4, 5]
    unique = [unique_list.append(x) for x in my_list if x not in unique_list]
    return unique_list

unique = unique_list()
print(unique)

#Sample Solution:
def unique_list1(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x

print(unique_list1([1,2,3,3,3,4,4,5,6]))


# def check_prime(num):
#     for x in range(2,num):
#         if num % x == 0:
#             return f"{num} is not a prime number."
#
#     return f"{num} is a prime number."



#print(check_prime(num = int(input("Check for a prime number: "))))


def check_even_numbers(sample_list):
    even = []
    for y in sample_list:
        if y % 2 == 0:
            even.append(y)
    return even

result = check_even_numbers([1,2,3,4,5,6,7,8,9])
print(f"Expected Result: {result}")


#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
def alph_order(string):
    b = string.split('-')
    b.sort()
    c = '-'.join(b)
    return c
a = input("Enter a sequence of colors separated with hyphen: ")
print(alph_order(a))

#Sample Solution:
items = [n for n in input(). split('-')]
items.sort()
print('-'.join(items)) #green-red-black-white (input)


people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people)