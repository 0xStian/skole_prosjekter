import hashlib

rockyou_file = open(input("Password list: "), 'r')
hash_file = open(input("List of Hashes: "), "r")

def get_hash():
    for line in hash_file:
        current_hash = line.strip()
        check_hashes(current_hash)

def check_hashes(current_hash):
    for line in rockyou_file:
        current_password = line.strip()
        current_password_hashed = hashlib.sha256(current_password.encode('utf-8')).hexdigest()
        if current_hash == current_password_hashed:
            print(f"Match Found! | {current_password_hashed} | {current_password}")
            return
        else:
            pass
        
get_hash()
