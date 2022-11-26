user_list = []
for x in range(10):
    user_list.append(f"{input('User:')}")
print(f"Sorted: {sorted(user_list)}")
username = input("Search User:")
if username in user_list:
    print(f"index: {sorted(user_list).index(username)}")
    print(f"reversed: {sorted(user_list, reverse=True)}")
    print(f"sliced: {sorted(user_list, reverse=True)[:5]}")
    user_list.append(input('Append new user:'))
    print(f"{user_list}")
else: 
    print("The user does not exist")