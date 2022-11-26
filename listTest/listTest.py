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
    length = len(sorted_list)
    middle_index = length//2
    sliced_list = sorted_list[:middle_index]
    print(f"Sliced list {sliced_list}")
    append_new_user()
    
    
def append_new_user():
    user_list.append(input("Append last user: "))
    display_original_list()


def display_original_list():
    print(f"Original list with new user {user_list}")


append_users()