# 1. Create a script called monthlyzip.py. Before writing the script, please create a new directory and copy a few text, image or sound files. In the script, do the following:
# Ask the user for the name of a new directory.
# Create the directory in the same path as the script.
# Copy all of the files from your pre-created directory to the new directory.
# Rename each newly created file by appending the original file’s creation date to the file name (before the file extension). This may require dusting off your string manipulation skills.
# Display the list of newly created files to the user by reading the contents of the new directory.
# Create a new zip file named according to today’s date and add the contents of the entire (new) directory to the zip file.
import os
import shutil
from datetime import datetime as dt
from datetime import date
import zipfile


# creates new dir, copies one dir's files to the new.
current_dir = os.getcwd() + "\\"
dir_to_copy = os.getcwd() + "\\random_path\\"
new_dir = input("New Directory Name: ") + "\\"
os.mkdir(current_dir + new_dir)
files_in_path = os.listdir(dir_to_copy)
# copies the files
for file in files_in_path:
    shutil.copy(dir_to_copy+file, current_dir+new_dir+file)
# renames the files to the date they were created
for file in os.listdir(current_dir+new_dir):
    new_files_metadata = os.stat(current_dir+new_dir+file)
    get_creation_time = f"{dt.fromtimestamp(new_files_metadata.st_ctime)}"
    new_filename = f"{current_dir}{new_dir}{file[:-4]}_{get_creation_time[20:]}.txt"
    os.rename(current_dir+new_dir+file, new_filename)
print(*os.listdir(current_dir+new_dir), sep="\n")
# create zip file and place files inside
date_today = date.today()
with zipfile.ZipFile(f"{current_dir}{date_today}.zip", "w") as zf:
    for file in os.listdir(current_dir+new_dir):
        zf.write(current_dir+new_dir+file)
