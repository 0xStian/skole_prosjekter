"""
1. Define a list 
2. Request 10 names of friends from the user and save them in the list. 
3. Sort the list. 
4. Ask the user for a name to search for. 
5. If the name exists in the list, display its index otherwise display the message “The name does not exist”. 
6. Reverse the list. 
7. Create a slice of the list consisting of the first half of the list entries. 
8. Display the contents of the slice. 
9. Ask the user for one more name. 
10. Append the name to the end of the original list. 
11. Display the contents of the original list. 
"""

user_list = []


def append_users():
    for x in range(10):
        user_list.append(f"{input('name: ')}")
    sort_list()


def sort_list():
    sorted_list = sorted(user_list)
    print(f"Sorted list {sorted_list}")
    search_user(sorted_list)
    
    
def search_user(sorted_list):
    username = input("Username to search for: ")
    if username in user_list:
        print(f"Usename {username} is at index: {sorted_list.index(username)}")
        reverse_list(sorted_list)
    else:
        print("The name does not exist")
            
      
def reverse_list(sorted_list):
    sorted_list.reverse()
    print(f"reversed list {sorted_list}")
    slice_list(sorted_list)


def slice_list(sorted_list):
    sliced_list = sorted_list[:5]
    print(f"Sliced list {sliced_list}")
    append_new_user()
    
    
def append_new_user():
    user_list.append(input("Append last user: "))
    display_original_list()


def display_original_list():
    print(f"Original list with new user {user_list}")


append_users()
