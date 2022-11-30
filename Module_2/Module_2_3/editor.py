"""
2.	Create a script named editor.py. In this script, prompt the user to enter a string of text.
    The following needs to happen until the user decides to exit the program, by pressing "e":
    
•	Display the current version of the input string to the user.  
•	Ask the user to select an option to be applied to the string: 
o	1: Uppercase 
o	2: Lowercase 
o	3: Titlecase 
o	4: Remove front and back whitespaces 
o	e: Exit program 
•	Update the string using the requested method or exit the program.
"""

user_input = input("enter string: ")
version = 1

while True:
    print("\n[1]: Uppercase\n[2]: Lowercase\n[3]: Titlecase\n[4]: Remove front and back whitespaces\n[e]: Exit program")
    user_choice = input("Choice (1, 2, 3, 4, e): ")
    print(f"\n[!] Version: {version}\n")
    version += 1
    if user_choice == "1":
        print(user_input.upper())
    elif user_choice == "2":
        print(user_input.lower())
    elif user_choice == "3":
        print(user_input.title())
    elif user_choice == "4":
        print(user_input.strip())
    elif user_choice == "e":
        quit()
    else:
        print("Invalid choice")
        version -= 1