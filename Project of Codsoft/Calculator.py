def calculator():
    print("Welcome to the basic arithmetic operations!")
    print("Please enter two numbers and choose an operation.")

    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))

    print("Choose operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation = input("Enter choice (1/2/3/4): ")

    if operation == '1':
        result = x + y
        print(f"The result is: {result}")
    elif operation == '2':
        result = x - y
        print(f"The result is: {result}")
    elif operation == '3':
        result = x * y
        print(f"The result is: {result}")
    elif operation == '4':
        if y != 0:
            result = x / y
            print(f"The result is: {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid input! Please try again.")

calculator()