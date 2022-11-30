delimiterStr= "Change my delimiter"
split = delimiterStr.split(" ")
print(*split, sep=";")
print(*split, sep=",")
print(*split, sep="|")

### alternative ###
# print(delimiterStr.replace(" ", ";"))
# print(delimiterStr.replace(" ", ","))
# print(delimiterStr.replace(" ", "|"))