#SIMPLE CALCULATOR WITH ADVANCE FEATURES
# Import the math module for exponentiation
import math

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

# Function to raise a number to a power
def exponentiate(x, y):
    return math.pow(x, y)

# Main function
def main():
    print("Welcome to Simple Calculator!\n")
    while True:
        print("Choose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exponentiation (^)")
        print("q. Quit (q)\n")
        
        choice = input("Enter your choice: ")
        
        if choice == 'q':
            print("\nThank you for using Simple Calculator!")
            break
        
        if choice in ('1', '2', '3', '4', '5'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}\n")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}\n")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}\n")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}\n")
            elif choice == '5':
                print(f"Result: {num1} ^ {num2} = {exponentiate(num1, num2)}\n")
        else:
            print("Invalid input. Please try again.\n")

if __name__ == "__main__":
    main()
