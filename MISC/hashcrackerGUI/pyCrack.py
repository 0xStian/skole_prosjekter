import hashlib
from time import sleep
import tkinter
list_of_results = []
    

def check_hash(password_list, hashes_list):
    with open(hashes_list, 'r', encoding='latin-1') as hashes_list:
        for line in hashes_list:
            current_hash = line.strip()
            if len(current_hash)==len(range(32)) and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                list_of_results.append(crack_hash(current_hash, "md5", password_list))

            elif len(current_hash)==len(range(128)) and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                list_of_results.append(crack_hash(current_hash, "sha512", password_list))

            elif len(current_hash)==len(range(64)) and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                list_of_results.append(crack_hash(current_hash, "sha256", password_list))

            elif len(current_hash)==len(40) and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                list_of_results.append(crack_hash(current_hash, "sha1", password_list))

            else:
                print(f"Could not Identify the hash type | {current_hash}")
        
        
def crack_hash(hash, hash_type, password_list):
    with open(password_list, 'r', encoding='latin-1') as password_list:
        for line in password_list:
            current_password = line.strip()
            match hash_type:
                case "md5": hashed_password = hashlib.md5(current_password.encode("utf-8")).hexdigest()
                case "sha1": hashed_password = hashlib.sha1(current_password.encode("utf-8")).hexdigest()
                case "sha256": hashed_password = hashlib.sha256(current_password.encode("utf-8")).hexdigest()
                case "sha512": hashed_password = hashlib.sha512(current_password.encode("utf-8")).hexdigest()
            if hashed_password == hash:
                print(f"{hash_type} | {hashed_password}:{current_password}")
                return f"{hash_type} | {hashed_password}:{current_password}"
        print(f"Could not find password for hash | {hash}")
        
def send_hash_and_passwords():
    try:
        check_hash(hashes_list=input("\n List Of Hashes > "), password_list=input(" Password List > "))
    except FileNotFoundError:
        input("[!] Cant find one of the files, Try Again! (Press Enter To Continue...)")
        send_hash_and_passwords()
    except KeyboardInterrupt:
        start()
    
def start():
    pass
