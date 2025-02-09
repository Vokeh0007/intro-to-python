# list comprehension
# list comprehension is a concise way to create lists in python.
#syntax [expression for item in iterable if condition]
#traditional loop
squares = []
for x in range(5):
    squares.append(x**2) #appending the square of x to the list
    print(squares)
    
#list comprehension
squares = [x**2 for x in range(5)]
print(squares)