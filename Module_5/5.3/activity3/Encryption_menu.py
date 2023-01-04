from cryptography.fernet import Fernet
import base64, os

key = base64.b64encode(b"thisisverysecretkeynobodycancrak")
fernet = Fernet(key)

def Menu():
    os.system("cls")
    choice = input("1. Encrypt a message \n2. Decrypt a message \n3. Exit\nEnter your choice: ")
    match choice:
        case "1": encrypt_message(input("Enter Message To Encrypt: "))
        case "2": decrypt_message()
        case "3": exit()
        case _: Menu()

def encrypt_message(message):
    encrypted_message = fernet.encrypt(message).encode()
    with open("encrypted.txt", "w") as file:
        file.write(f"{encrypted_message.decode('utf-8')}")
    os.system("cls")
    print("\nEncrypted message saved to encrypted.txt\n")
    input("Press enter to go back to the menu...")
    Menu()
    
    
def decrypt_message():
    with open("encrypted.txt", "r") as file:
        encrypted_message = file.read()
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    os.system("cls")
    print("\nEncrypted message was: " + decrypted_message)
    input("Press enter to go back to the menu...")
    Menu()

Menu()