import hashlib

password_list = input("Password list (rockyou.txt): ")
hashes_file = input("List of Hashes (hashes.txt): ")


def check_hash(password_list, hashes_list):
    with open(hashes_list, 'r', encoding='latin-1') as hashes_list:
        for line in hashes_list:
            current_hash = line.strip()
            if len(current_hash)==len('ae11fd697ec92c7c98de3fac23aba525') and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                crack_hash(current_hash, "md5", password_list)
            elif len(current_hash)==len('ea8e6f0935b34e2e6573b89c0856c81b831ef2cadfdee9f44eb9aa0955155ba5e8dd97f85c73f030666846773c91404fb0e12fb38936c56f8cf38a33ac89a24e') and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                crack_hash(current_hash, "sha512", password_list)
            elif len(current_hash)==len('2c740d20dab7f14ec30510a11f8fd78b82bc3a711abe8a993acdb323e78e6d5e') and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                crack_hash(current_hash, "sha256", password_list)
            elif len(current_hash)==len('4a1d4dbc1e193ec3ab2e9213876ceb8f4db72333') and current_hash.isdigit()==False and current_hash.isalpha()==False and current_hash.isalnum()==True:
                crack_hash(current_hash, "sha1", password_list)
            else:
                print(f"Could not Identify the hash type | {current_hash}")
        
    
def crack_hash(hash, hash_type, password_list):
    with open(password_list, 'r', encoding='latin-1') as password_list:
        for line in password_list:
            try:
                current_password = line.strip()
                if hash_type == "md5":
                    hashed_password = hashlib.md5(current_password.encode("utf-8")).hexdigest()
                elif hash_type == "sha1":
                    hashed_password = hashlib.sha1(current_password.encode("utf-8")).hexdigest()
                elif hash_type == "sha256":
                    hashed_password = hashlib.sha256(current_password.encode("utf-8")).hexdigest()
                elif hash_type == "sha512":
                    hashed_password = hashlib.sha512(current_password.encode("utf-8")).hexdigest()
                else:
                    print("[!] error while hashing password in password list")
            except:
                print("[!] error while hashing password in password list")

            if hashed_password == hash:
                print(f"{hash_type} | {hashed_password}:{current_password}")
                return
        print(f"Could not find password for hash | {hash}")
        
check_hash(password_list="rockyou.txt", hashes_list="hashes.txt")