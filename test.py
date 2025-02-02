number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number1[1:5]) # [2, 3, 4, 5]
print(number1[1:5:2]) # [2, 4] sequence[start:stop:step]
print(number1[::2]) # [1, 3, 5, 7, 9] sequence[start:stop:step]
print(number1[::-1]) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] sequence[start:stop:step]
print(number1[5:2:-1]) # [6, 5, 4] sequence[start:stop:step]
print(number1[5:2]) # [] sequence[start:stop:step]


numbers = [21, 34, 23, 12]
print("Before Append:", numbers ) # append adds an element to the end of the list
numbers.append(65)
print("After Append:", numbers) # [21, 34, 23, 12, 65]


prime_numbers = [2, 3, 5]
print("list 1:", prime_numbers)

even_numbers = [4, 6, 8]
print("list 2:", even_numbers)

even_numbers.extend(prime_numbers) # extend adds elements of a list to another list

print("After Extend:", even_numbers)


languages = ['Python', 'Java', 'C++', 'JavaScript']
print("Before Insert:", languages) # insert adds an element at a specified index no replacing
languages.insert(1, 'Ruby')
print("After Insert:", languages) # ['Python', 'Ruby', 'Java', 'C++', 'JavaScript']

"""language = ['Python', 'Java', 'C++', 'JavaScript']
language[2] = 'C' # replace an element at a specified index
del language[3] # delete an element at a specified index
del language[1:3] # delete elements in a specified range
del language [-1] # delete the last element
language.remove('Java') # remove an element by value
print(language)"""

'''
method                      description
append()                    Adds an element to the end of the list
extend()                    Adds elements of a list to another list
insert()                    Adds an element at a specified index
remove()                    Removes an element by value
pop()                       Removes an element at a specified index
clear()                     Removes all elements from the list
index()                     Returns the index of the first occurrence of an element
count()                     Returns the number of occurrences of an element
sort()                      Sorts the list in ascending order by default
reverse()                   Reverses the list
copy()                      Returns a copy of the list
'''

#iterating through a list
langi = ['Python', 'Java', 'C++', 'JavaScript']
for language in langi:
    print(language)
    
#iterating through a list with index
lang = ['Python', 'Java', 'C++', 'JavaScript']
for index, language in enumerate(lang):
    print(index, language)
    
    
# list comprehension
num = [1, 2, 3, 4, 5]
squared = [n**2 for n in num]
print(squared) # [1, 4, 9, 16, 25]

numb = [number*number for number in range(1, 7)]
print(numb) # [1, 4, 9, 16, 25, 36]


# list comprehension with condition
numbe = [1, 2, 3, 4, 5]
even = [n for n in numbe if n % 2 == 0]
print(even) # [2, 4]

#tuple
# A tuple is a collection of ordered and immutable elements enclosed in parentheses ()
# A tuple can have elements of different data types
# A tuple can be created with or without parentheses
var1 = ("hello")
print(type(var1)) # <class 'str'>
var2 = "hello"
print(type(var2)) # <class 'str'>
var3 = ("hello",)
print(type(var3)) # <class 'tuple'>
var4 = "hello",
print(type(var4)) # <class 'tuple'>

#indexing normal way -1 last item -2 second last item and so on
#one cannot use add or remove methods on a tuple    

my_tuple = (1, 2, 3, 4, 5, 3, 3)
print(my_tuple[1]) # 2
print(my_tuple[-1]) # 5
print(my_tuple[1:4]) # (2, 3, 4)
print(my_tuple.count(3)) # 1
print(my_tuple.index(3)) # 2 # returns the index of the first occurrence of an element


#unpacking a tuple
# Unpacking a tuple assigns its elements to multiple variables
person = ("John", 25, "Engineer")
name, age, occupation = person
print(name)
print(age)
print(occupation)


#Dictionary
# A dictionary is a collection of unordered, mutable, and indexed elements enclosed in curly braces {}
# A dictionary has key-value pairs
captain = {'team': 'India', 'captain': 'Virat Kohli', 'ranking': 2}
print(captain['ranking'])
print(captain.get('captain'))

info = {1: 'John', 2: 'Jane', 3: 'Joe'}
print(info)
print(info[1])

number = {1: 'one', 2: 'two', 3: 'three'}
print(number)
print(number.get(1)) # one

#adding a key-value pair
captain['best-player'] = 'four'
print(captain) 

#updating/changing a key-value pair/element
captain['ranking'] = 1
print(captain)

student_id = {111: 'John', 112: 'Jane', 113: 'Joe'}
print("initial dictionary:", student_id)
del student_id[113]
print("after deletion:",student_id)
student_id.clear()
print("after clearing:", student_id)

'''
method                      description
get()                       Returns the value of a specified key
pop()                       Removes an element with a specified key
popitem()                   Removes the last inserted key-value pair
keys()                      Returns the keys of the dictionary
values()                    Returns the values of the dictionary
items()                     Returns the key-value pairs of the dictionary
update()                    Updates the dictionary with another dictionary
copy()                      Returns a copy of the dictionary
clear()                     Removes all elements from the dictionary
sorted()                    Returns a new sorted list of keys
len()                       Returns the number of key-value pairs
any()                       Returns True if any key of the dictionary is true
all()                       Returns True if all keys of the dictionary are true

'''

#merging two dictionaries
dict1 = {1: 'one', 2: 'two'}
dict2 = {3: 'three', 4: 'four'}
dict1.update(dict2)
print(dict1)


#iterating through a dictionary
student = {1: 'John', 2: 'Jane', 3: 'Joe'}
for key in student:
    print(key, student[key])


#dictionary comprehension
squared = {x: x*x for x in range(6)}
print(squared) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#membership in dictionary
student = {1: 'John', 2: 'Jane', 3: 'Joe'}
print(1 in student) # True
print( 2 not in student) # False
print('John' in student) # False # only keys are checked not values    


#Set
# A set is a collection of unordered and unindexed elements enclosed in curly braces {}
# A set does not allow duplicate elements
# A set can have elements of different data types
# A set is mutable
# A set can be created with or without curly braces
# A set can be created using the set() constructor
# A set cannot be indexed
# A set can be iterated using a loop or list comprehension
# A set can have elements of different data types
# Using curly braces
fruits = {"apple", "banana", "cherry"}
print(fruits)  # Output: {'banana', 'cherry', 'apple'} (order may vary)

# Using set() function
numbers = set([1, 2, 3, 4, 4, 2])
print(numbers)  # Output: {1, 2, 3, 4} (duplicates are removed)

fruits.add("orange")  # Adds 'orange' to the set
print(fruits)  

fruits.remove("banana")  # Removes 'banana' (Raises an error if not found)
fruits.discard("mango")  # Removes 'mango' (No error if not found)
print(fruits)

fruits.clear()  # Removes all elements
print(fruits)   # Output: set()


#set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2  # or set1.union(set2) Elements from both sets.
print(union_set)  # Output: {1, 2, 3, 4, 5}

intersect_set = set1 & set2  # or set1.intersection(set2) Elements common to both sets.
print(intersect_set)  # Output: {3}

diff_set = set1 - set2  # or set1.difference(set2) Elements in set1 but not in set2.
print(diff_set)  # Output: {1, 2}

difff_set = set2 - set1 # or set2.difference(set1) Elements in set2 but not in set1.
print(difff_set) # Output: {4, 5}

sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2) Elements in either set, but not both.
print(sym_diff_set)  # Output: {1, 2, 4, 5}

#Checking membership in a set
number2 = {1, 2, 3, 4, 5}
print(3 in number2)   # Output: True
print(10 in number2)  # Output: False
print(2 not in number2) # Output: False

#looping through a set
for fruit in {"apple", "banana", "cherry"}:
    print(fruit)  # Prints each fruit (order is unpredictable)

frozen_numbers = frozenset([1, 2, 3, 4])
# frozen_numbers.add(5)  # ❌ Error: Frozen sets cannot be modified
print(frozen_numbers)


'''
Method              	            Description
add(x)	                            Adds x to the set
remove(x)	                        Removes x, raises error if not found
discard(x)	                        Removes x, no error if not found
clear()	                            Removes all elements from the set
union(set2)	                        Combines sets (`set1
intersection(set2)	                Returns common elements (set1 & set2)
difference(set2)	                Returns elements in set1 but not in set2 (set1 - set2)
symmetric_difference(set2)	        Elements in either set, but not both (set1 ^ set2)
copy()	                            Returns a copy of the set
isdisjoint(set2)	                Returns True if no common elements
issubset(set2)	                    Returns True if all elements of set1 are in set2
issuperset(set2)	                Returns True if all elements of set2 are in set1
pop()	                            Removes and returns an arbitrary element
len()	                            Returns the number of elements
any()	                            Returns True if any element is true
all()	                            Returns True if all elements are true
'''
'''
Key Takeaways
✅ Unordered – No specific order of elements.
✅ Unique Elements – Duplicates are automatically removed.
✅ Fast Membership Checking – in is much faster than in lists.
✅ Supports Mathematical Operations – Union, intersection, etc.
✅ Mutable – Can be modified, except frozenset.
'''


#strings
# A string is a sequence of characters enclosed in single, double, or triple quotes
# A string is immutable
# A string can be indexed and sliced

# Creating strings
string1 = 'Hello, World!'
string2 = "Hello, World!"
string3 = '''Hello, World!'''
string4 = """Hello, World!"""
print(string1)
print(string2)
print(string3)
print(string4)

# Accessing characters in a string
string = "Hello, World!"
print(string[1])  # Output: e
print(string[-1])  # Output: !
print(string[7:12])  # Output: World

# String methods
string = "Hello, World!"
print(string.upper())  # Output: HELLO, WORLD!
print(string.lower())  # Output: hello, world!
print(string.replace("H", "J"))  # Output: Jello, World!
print(string.split(","))  # Output: ['Hello', ' World!']

# String concatenation
string11 = "Hello"
string12 = "World"
print(string11 + string12)  # Output: HelloWorld

# String formatting
name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")

#multiline strings
string = """
This is a
multiline string
"""
print(string)

#string slicing
string = "Hello, World!"
print(string[2:5])  # Output: llo
print(string[:5])  # Output: Hello
print(string[7:])  # Output: World!
print(string[-5:-1])  # Output: orld

#string operations
string = "Hello, World!"
print("Hello" in string)  # Output: True
print("World" not in string)  # Output: False
print(len(string))  # Output: 13
#comparing two strings
string1 = "Hello, World!"
string2 = "Hello, World!"
print(string1 == string2)  # Output True
#joining strings
string = "Hello, World!"
print(" ".join(string))  # Output: H e l l o ,   W o r l d !
#reversing a string
string = "Hello, World!"
print(string[::-1])  # Output: !dlroW ,olleH


#iterating through a string
for char in "Hello":
    print(char)
    
'''
method                      description
upper()                     Converts the string to uppercase
lower()                     Converts the string to lowercase
replace()                   Replaces a string with another string
split()                     Splits the string into a list
join()                      Joins elements of a list into a string
find()                      Returns the index of the first occurrence of a substring
count()                     Returns the number of occurrences of a substring
startswith()                Returns True if the string starts with a specified substring
endswith()                  Returns True if the string ends with a specified substring
isalpha()                   Returns True if all characters are alphabets
isdigit()                   Returns True if all characters are digits
isalnum()                   Returns True if all characters are alphanumeric (alphabets or digits)
isspace()                   Returns True if all characters are whitespaces
strip()                     Removes leading and trailing whitespaces from the string
lstrip()                    Removes leading whitespaces from the string
rstrip()                    Removes trailing whitespaces from the string
capitalize()                Converts the first character to uppercase
title()                     Converts the first character of each word to uppercase
swapcase()                  Swaps the case of each character
center()                    Returns a centered string
ljust()                     Returns a left-justified string
rjust()                     Returns a right-justified string
zfill()                     Fills the string with zeros

'''

#escape sequences
# An escape sequence is a sequence of characters that represents a special character
# Escape sequences start with a backslash (\)
# Escape sequences are used to represent characters that are difficult or impossible to type
example = "Hello, \"World!\""
print(example)  # Output: Hello, "World!"

'''
escape sequence     description
\\                  Backslash (\)
\'                  Single quote (')
\"                  Double quote (")
\n                  New line
\t                  Tab
\b                  Backspace
\r                  Carriage return
\f                  Form feed
\v                  Vertical tab
\ooo                Octal value
\xhh                Hex value
'''