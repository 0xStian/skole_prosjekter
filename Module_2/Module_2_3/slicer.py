"""
Create a script name slicer.py. In this script, prompt the user to enter a string of text,
an index inside the string where a substring should start and an index inside the string where the substring should end.
Make use of what you know of error handling to ensure that if a start index is outside of the bounds of the string it is set to the
first element / character in the string and if an end index is set outside of the bounds of the string it is set to the last element / character in the string.
Display the substring to the user.
"""

user_input = input("enter input: ")
index_start = input("enter start index: ")
index_end = input("enter end index: ")

splitted = [*user_input]

if len(user_input) > index_start | len(user_input) < index_end:
    print(user_input[int(index_start):int(index_end)])
else:
    print("Index out of range")