from cryptography.fernet import Fernet
import base64


key = base64.b64encode(b"thisisverysecretkeynobodycancrak")
fernet = Fernet(key)

encrypted_message = fernet.encrypt(input("Enter a very secret message to encrypt: ").encode())

with open("encrypted.txt", "w") as file:
    file.write(f"{encrypted_message.decode('utf-8')}")
    
print("Encrypted message saved to encrypted.txt")
input("Press enter to exit!")
exit()