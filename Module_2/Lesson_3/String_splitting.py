"""
Given the below variable and string assignment, use it in your Python script and print the indexes in the following order 16,15,4,17,6,12,11,18.
You must use the Python split() function to split the string.
"""

strmessage =  "what,is,not,good,I,will,be,you,ok,Noroff,student,Python,a,awesome,pretty,knew,who,would,programmer"
default_order = [16,15,4,17,6,12,11,18]
split = strmessage.split(",")
for x in default_order:
    print(split[x], end=" ")