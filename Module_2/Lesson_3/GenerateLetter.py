"""
Create a script called GenerateLetter.py. In the script, create a function called generate_letter which is to serve as a generator function.
The generator should return a letter in the range a to e. If the generator returns the letter e, it should return the letter a the next time the generator function object is used.
Demonstrate the use of the generator in the main portion of your script by display the letters a to e twice.
"""
import random
from time import sleep

def generate_letter():
    last_letter = ""
    while True:
        letters = ["a", "b", "c", "d", "e"]
        if last_letter == "e":
            print("a")
            last_letter = "a"
        else:
            random_letter = random.choice(letters)
            last_letter = random_letter
            print(random_letter)
        sleep(1)
    
    
generate_letter()