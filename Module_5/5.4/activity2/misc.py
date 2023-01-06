import os

def menu():
    os.system("cls")
    print("1. Scan a network.")
    print("2. Scan a device for open ports.")
    print("3. Save results to a CSV (Comma separate value) file.")
    print("4. Exit.")
    choice = input("Enter your choice >")
    return choice
