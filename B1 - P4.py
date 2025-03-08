#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 4 - PRODUCT
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the product of two numbers.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\nThe product of {num_1} and {num_2} is equal to {num_1 * num_2: .2f}.")

