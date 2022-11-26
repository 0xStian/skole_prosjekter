"""
1. -Define a set 
2. -Populate the set with the names of your 5 favourite fast foods (no user input required). 
3. -Define a second set and populate it with the names of a friend’s 5 favourite fast foods (no user input required). 
4. -Add another type of fast food to your set of favourite foods. 
5. -Determine which favourite fast foods are shared by you and your friend and display these overlapped foods. 
"""

fastfood_set = {"mcdonalds", "starbucks", "wendys", "tacobell", "subway"}
friends_fastfood_set = {"chick_fil_a", "dominos", "kfc", "starbucks", "chipotle"}

fastfood_set.add(str(input("add new fastfood: ")))

for x in fastfood_set:
    if x in friends_fastfood_set:
        print(f"shared fastfood: {x}")