'''
What is a Function?

A function is a block of code designed to perform a specific task. You define a function once and can use it multiple times throughout your code.
'''
# syntax#


def function_name(parameters):
    """Optional docstring explaining the function."""
    # Code block
    return Value  # Optional return statement

# Types of Functions
# Built-in Functions: Predefined functions in Python (e.g., print(), len(), type()).
# User-defined Functions: Functions created by the user.

# defining and calling of a function


def greet(name):
    '''Great a person by their name'''
    return f'Hello, {name}!'


print(greet('Alice'))


# Key Components of a Function
'''
Function Name: Should be descriptive and follow naming conventions.
Parameters: Variables passed into the function.
Docstring: An optional description of what the function does.
Return Statement: Outputs a value from the function (optional).
'''

# Parameters and Arguments

# Functions can accept zero or more arguments.

# 1. Positional Arguments:


def add(a, b):
    return a+b


print(add(3, 4))

# 2 default arguments


def greet(name='Guest'):
    return f'hello, {name}!'


print(greet())
print(greet('Alice'))

# 3. Keyword Arguments


def introduce(name, age):
    return f"My name is {name}, and Iam {age} years old."


print(introduce(age=25, name="bob"))

# returning values


def add(a, b):
    return a+b


result = add(3, 4)
print(result)


def square(number):
    return number**2


result = square(4)
print(result)


# anonymous functions: lambda
# Syntax: lambda arguments: expression
def add(x, y): return x + y


print(add(3, 5))

# using lambda with map
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)


# recursive functions -- a function that calls itself
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


# Scope of Variables
'''
Local Variables: Variables defined inside a function.
Global Variables: Variables defined outside a function.
'''


def add(a, b):
    result = a + b
    return result


print(add(3, 4))

# Global Variables
name = 'Alice'


def greet():
    return f'Hello, {name}!'


print(greet())

# benefits of functions
'''
1. Code Reusability: Functions can be called multiple times.
2. Modular Code: Functions make code more organized and easier to read.
3. Debugging: Functions help in debugging and troubleshooting code.
4. Improved Readability: Descriptive names make code easier to understand.
'''
# quiz one
'''Create a function named large_power() that takes two parameters named base and exponent.
If base raised to the exponent is greater than 5000, return True, otherwise return False '''


def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False


print(large_power(20, 3))

# quiz two
'''
Create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

Define the function header to accept one input num
Calculate the remainder of the input divided by 10 (use modulus)
Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False
'''


def is_divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False


print(is_divisible_by_ten(22))
