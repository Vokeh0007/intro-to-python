#variables
#variables are containers for storing data values

site_name = "plp"
print (site_name)
#assigning a new value to the variable
site_name = "Ilove coding"
print (site_name)

a,b,c = 5,7, "hello world"
print (b) #7
print (c) #hello world
print (a) #5

# rules for variable names
## snake_case
##MACRO_CASE
##camelCase
##CapWords

#PYTHON IS CASE SENSITIVE
#LIST DATA TYPE
#List is a collection which is ordered and changeable. Allows duplicate members.
languages = ["python", "c", "c++", "javascript"]
print (languages)
print (languages[0])
print (languages[1])

#change the value of a list
languages[0] = "java"
print (languages)

# tuple data type
#A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#In Python tuples are written with round brackets.
fruits = ("apple", "banana", "cherry")
print (fruits)
#accessing tuple items
print (fruits[0])
print (fruits[1])


#string data type
#strings in python are surrounded by either single quotation marks, or double quotation marks.
site_name = "Power Learn Project"
print(site_name)

#string slicing
#You can return a range of characters by using the slice syntax.
#Specify the start index and the end index, separated by a colon, to return a part of the string.
site_name = "Power Learn Project"
print (site_name[2:4]) #we

#set data type --indexing has no meaning
#A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
fruits = {"apple", "banana", "cherry"}
print (fruits)

#dictionary data type
#A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.
capital = {"Kenya": "Nairobi", "Uganda": "Kampala"}
print(capital)

#datatypes in python
#numeric -- int, float, complex
#sequence -- list, tuple, range
#mapping -- dictionary
#set -- set, frozenset
#boolean -- bool
#binary -- bytes, bytearray, memory
#string -- str



