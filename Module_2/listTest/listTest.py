"""
1. Define a list.
2. Request 10 names of friends from the user and save them in the list.
3. Sort the list.
4. Reverse the list.
5. Ask the user for one more name.
6. Append the name to the end of the original list.
7. Display the contents of the original list.
"""

user_list = []
for x in range(10):
    user_list.append(input('User: '))
print(f"Sorted: {sorted(user_list)}")
username=input("Username to search for: ")
if username in user_list:
    print(f"index: {sorted(user_list).index(username)} \nreversed: {sorted(user_list, reverse=True)} \nsliced: {sorted(user_list, reverse=True)[:5]}")
    user_list.append(input('Append new user: '))
    print(f"{user_list}")
else:
    print("The name does not exist")