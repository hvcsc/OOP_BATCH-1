#NAME: ARAG, JIREH CAMILLE S.
#PROGRAM: PROG 10
#DATE: MARCH 2025

print("This program prints all the numbers from 0 to 100 except numbers ending in zero.")

for num in range(1, 101): #start, stop
    if num % 10 != 0:
        print(num)