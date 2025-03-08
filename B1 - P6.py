#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 6 - EXPONENTIATION
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program computes exponentiation.")

num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\n{num_1} raised to the power of {num_2} is equal to{num_1 ** num_2: .2f}.")