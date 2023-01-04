import os, sys, imagehash
from PIL import Image

#finds all files in folder
def scan_folder_for_files(folder):
    file_list = []
    try:
        for root, dirs, files in os.walk(folder):
            for file in files:
                file_list.append(os.path.join(root, file))
        return file_list
    except:
        print("Error scanning folder: " + folder)
        exit()

#hashes x file in folder and returns hash
def hash_pictures_in_folder(picture):
    try:
        return str(imagehash.average_hash(Image.open(picture)))
    except:
        print("Error hashing file: " + picture)


#checks if there are any duplicates in the list and prints them to a file if there are any
def check_for_duplicates(hashed_pictures, output):
    for hash in hashed_pictures:
        hashed_pictures.remove(hash)
        if hash in hashed_pictures:
            print("[*] Duplicate found!     | Hash: " + hash)
            with open(output, "a") as file:
                file.write(f"[*] Duplicate found! | Hash: {hash}\n")
        else:
            print("[-] No duplicates found! | Hash: " + hash)
            hashed_pictures.append(hash)
    input("Press enter to exit!")
    
 
#checks if the arguments are valid and sets the folder to scan and the path to save to
try:
    if sys.argv[1] == "--path" or "-p":
        folder_to_scan = sys.argv[2]
        if sys.argv[3] == "--output" or "-o":
            output = sys.argv[4]
        else:
            print("Invalid argument")
    else:
        print("Invalid argument")
except:
    print("Usage: Check_images_for_duplicates --path <folder_to_scan> --output <output_file>")
    print("Aternative Usage: Check_images_for_duplicates -p <folder_to_scan> -o <output_file>")
    exit()
    
#sends folder to scan function and adds the result to a list
pictures = scan_folder_for_files(folder_to_scan)
#sends images to hash function and adds the result to a list
hashed_pictures = []
for pic in pictures:
    hashed_pictures.append(hash_pictures_in_folder(pic))
#sends the list to check for duplicates function
check_for_duplicates(hashed_pictures, output)