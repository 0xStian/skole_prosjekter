user_input = input("Enter String: ")
split_input = user_input.split(" ")
for x in split_input:
    if x == "good":
        split_input[split_input.index(x)] = "great"
    if x == "bad":
        split_input[split_input.index(x)] = "perfect"
print(*split_input, end=" ")