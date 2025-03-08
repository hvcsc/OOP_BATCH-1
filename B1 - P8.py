#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 8 - ODD NUMBER
#DATE: MARCH 2025

def number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Enter a numeric value.")

print("This program prints the total of odd numbers from the given values.")

nums = [number(f"Enter number {i +1}: ") for i in range(10)]
odd = sum(1 for num in nums if num % 2 != 0)

print(f"\nThe total of odd numbers in the given value is {odd}.")