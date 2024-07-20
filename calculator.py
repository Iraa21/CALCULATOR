def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def calculator():
    print("SIMPLE CALCULATOR")
    print("=================")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    while True:
        try:
            choice = int(input("Enter operation number (1/2/3/4): "))
            if choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == 1:
        result = add(num1, num2)
        operation = "+"
    elif choice == 2:
        result = subtract(num1, num2)
        operation = "-"
    elif choice == 3:
        result = multiply(num1, num2)
        operation = "*"
    elif choice == 4:
        result = divide(num1, num2)
        operation = "/"
    
    print(f"{num1} {operation} {num2} = {result}")

calculator()
