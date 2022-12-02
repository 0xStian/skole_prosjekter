"""
Use the below string, and create a Python script that will change the delimiter from a space to a 1) semicolon (;) 2) a comma (,) and 3) the pipe character (|).
“Change my delimiter”
"""

delimiterStr= "Change my delimiter"
split = delimiterStr.split(" ")
print(*split, sep=";")
print(*split, sep=",")
print(*split, sep="|")

### alternative ###
# print(delimiterStr.replace(" ", ";"))
# print(delimiterStr.replace(" ", ","))
# print(delimiterStr.replace(" ", "|"))