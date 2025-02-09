#types of loops
#while loop
# for loop
#iteration in python
#indefinite iteration -- where the number of times the loop is executed depends on how many times a condition is met.
#definite iteration -- where the number of times the loop is executed is specified explicitly.

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I love {fruit}!")

# for loop with range
for number in range(1, 5):
    print(f"Number: {number}")
    
    
# while loop
count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1
    
#loop controls
#break statement
for number in range(1, 10):
    if number == 5:
        print("breaking the loop at 5")
        break 
    elif number % 2 == 0:
        print(f"Skipping {number} because it is even")
        continue
    print(f"Procesing number {number}")
    
#nested loops
# nested loops example
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i: {i}, j: {j}")
        