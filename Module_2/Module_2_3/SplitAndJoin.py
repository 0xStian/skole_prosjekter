"""
Create a script named splitandjoin.py. In this script, prompt the user to enter a string of text.
Next ask the user for a character on which to split their text. Use this character to split their initial string.
Display the elements of the split string to the user. Request text from the user to use in order to re-combine the string.
Display the re-combined string to the user.
"""

user_input = input("string: ")
character_to_split = input("character to split: ")
splitted = user_input.split(character_to_split)
print(*splitted)
recombine_character = input("character to replace splitted: ")
print(*splitted, sep=recombine_character)





# print(user_input.replace(character_to_split, f"{character_to_split} "))