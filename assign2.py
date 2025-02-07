#Tasks:

'''Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.'''

numbers = input("Enter a list of integers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
total_sum = sum(numbers)
print(f"The sum of the numbers is: {total_sum}")


#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

fav_books = ("Ghost face", "laws of power", "subtle art of not giving a f*ck", "the alchemist", "the secret")
for book in fav_books:
    print(book)


#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
person = {'name': input("Enter your Name: "), 'age' : input("Enter your Age: " ), 'fav_color': input("Enter your favorite color: ")}
print(person)


#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
set1 = set(map(int, input("Enter list of integers separated by space: ").split()))
set2 = set(map(int, input("Enter list of integers separated by space: ").split()))
intersect_set = set1 & set2
print(f"The common elements are: {intersect_set}")

#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

words = ["apple", "mango", "orange", "banana", "grapes"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print(odd_length_words)

