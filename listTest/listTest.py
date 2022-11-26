user_list = []
for x in range(10): user_list.append(f"{input('User: ')}")
print(f"Sorted: {sorted(user_list)}"); username = input("Username to search for: ")
if username in user_list: print(f"index: {sorted(user_list).index(username)}\nreversed: {sorted(user_list, reverse=True)}\nsliced: {sorted(user_list, reverse=True)[:5]}"); user_list.append(input('Append new user: ')); print(f"{user_list}")
else: print("The name does not exist")