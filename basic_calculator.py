# Basic calculator 

def add(num1, num2):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

def subtraction(num1, num2):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

def multiplication(num1, num2):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

def division(num1, num2):
    try:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

while True:
    try:
        print("\nBasic Calculator")
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")
        
        choice = input("Enter your choice (A/B/C/D/E): ").upper()
    
        if choice == "A":
            print("Addition")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            add(num1, num2)

        elif choice == "B":
            print("Subtraction")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            subtraction(num1, num2)

        elif choice == "C":
            print("Multiplication")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            multiplication(num1, num2)

        elif choice == "D":
            print("Division")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            division(num1, num2)

        elif choice == "E":
            exit()

        else:
            print("Invalid input. Please select a valid option.")

    except ValueError:
        print("Error: Please enter a valid numeric value!")
    except Exception as e:
        print("An unexpected error occurred:", e)
