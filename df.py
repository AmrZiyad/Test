# 1. Define the 4 arithmetic functions
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    # The requirement asks to handle ZeroDivisionError using try/except
    if num2 == 0:
        raise ZeroDivisionError("Error: Cannot divide by zero.")
    return num1 / num2

def main():
    print("Function Calculator")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice not in ['1', '2', '3', '4']:
        print("Invalid operation choice.")
        return

    # 2. Use try/except block to catch ValueError and ZeroDivisionError
    try:
        # 3. Use float(input()) to read numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")
            
    except ValueError:
        print("Error: Invalid input. Please enter valid numerical values.")
    except ZeroDivisionError as e:
        print(e)

# Run the calculator program
if __name__ == "__main__":
    main()
