#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 1 - BIGGER NUMBER
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the bigger value between two numbers.")
num_1 = number("\nEnter the first number: ")
num_2 = number("Enter the second number: ")

print(f"\n{max(num_1, num_2)} is bigger than {min(num_1, num_2)}.")

