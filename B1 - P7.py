#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 7 - SUMMATION
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the sum of the given values.")
nums = [number(f"Enter number {i + 1}: ") for i in range(10)]
print(f"\nThe sum of all numbers is {sum(nums): .2f}.")