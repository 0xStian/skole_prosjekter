from cryptography.fernet import Fernet
import base64


key = base64.b64encode(b"thisisverysecretkeynobodycancrak")
fernet = Fernet(key)

with open("encrypted.txt", "r") as file:
    encrypted_message = file.read()
    
decrypted_message = fernet.decrypt(encrypted_message).decode()

print("Encrypted message was: " + decrypted_message)
input("Press enter to exit!")
exit()