"""
Write a Python script that will replace the word 'good' with 'great', and 'bad' with 'perfect' in a string.
Ask the user for input, perform the replacement and then output the modified string.
"""

user_input = input("Enter String: ")
split_input = user_input.split(" ")
for x in split_input:
    if x == "good":
        split_input[split_input.index(x)] = "great"
    if x == "bad":
        split_input[split_input.index(x)] = "perfect"
print(*split_input, end=" ")