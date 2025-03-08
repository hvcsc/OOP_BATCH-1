#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 3 - SUM
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the sum of two numbers.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\nThe sum of {num_1} and {num_2} is equal to {num_1 + num_2}.")
