"""
Create a script that will underline any length of a string. Use the below string as a start. Only 1 “-“ can be used for the print function.
If you change the string, the print function should underline the new string without you needing to change the print function. 
The script should print the string and then print the “-“ characters underneath the string, to the same length as the original string.  
"""

strUnderline = "This sentence must be underlined"
print(strUnderline)
for x in range(len(strUnderline)):
    print("-", end="")
    