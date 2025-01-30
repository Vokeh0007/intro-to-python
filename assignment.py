def calculate(num1, num2,operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1/num2
        else:
            return "Error! division by zero."
    else:
        return "Invalid Opeartion."
    
while True:
    # user inputting
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter opearation sign (+, -, *, /): ")

    #perfoming operation and outputting
    result = calculate(num1, num2, operation)
    print(f"{num1} {operation} {num2} = {result}")

    #for more calculations
    another_calculation = input("Do you wish to perfom another calculation? (yes/no): ").lower()
    if another_calculation != 'yes':
        print("Thank you for using the calculator!😊")
        break