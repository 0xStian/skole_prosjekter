"""
Create a script called PrintPerfect.py. Create a script that requests a maximum integer from the user.
The script should then calculate every perfect number from 1 to the maximum value entered by the user.
A number is perfect if it is equal to the sum of all the smaller integers that divide equally into it.
6 is a perfect number, because 1, 2 and 3 all divide equally into it and 1 + 2 + 3 = 6.
"""

max_integer = int(input("Enter Max Integer: "))
        
for i in range(1, max_integer + 1):
    sum1 = 0
    for x in range(1, i):
        if i % x == 0:
            sum1 += x
            if sum1 == i:
                print(f"{i} is a pefect number")