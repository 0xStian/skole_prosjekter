"""
Create a script named editor.py. In this script, prompt the user to enter a string of text. The following needs to happen: Display the length of the string.
Ask the user for an index in the string. Display the string entered by the user, BUT add single quotes (“) around the word *of the index* that the user entered on the previous option.
"""

user_input = input("string: ")
index = int(input("index: "))
splitted = user_input.split(" ")
word = splitted[index]
splitted[index] = f"*{word}*"
print (*splitted, sep=" ")
