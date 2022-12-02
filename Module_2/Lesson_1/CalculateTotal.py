"""
Create a script called CalculateTotal.py. The script should continuously ask a user to enter an integer value.
This should continue until the user has entered the value -1. Once the loop has ended print the total of all the values entered by the user (excluding -1).
"""

user_input = 0
total_sum = 0
while user_input != -1:
    user_input = int(input("Enter Integer: "))
    total_sum += user_input
print(f"sum: {total_sum + 1}")