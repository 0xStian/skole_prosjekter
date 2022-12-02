"""
Create a Python script called mymodules.py. In this script create the following functions:
•	create_time: This function should create a time object and return it. 
•	output_local_time: This function should receive a time object as a parameter and display the local_time associated with it. 
•	calculate_difference: This function should receive two objects, subtract them from each other and return the difference. 
•	generate_random: This function receives a maximum number as a parameter and then returns a random number between 0 and the maximum number.
"""
import time
import random

def create_time():
    current_time = time.time()
    return current_time

def output_local_time():
    current_localtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
    return current_localtime

def calculate_difference(n1, n2):
    difference = n1 - n2
    return difference
    

def generate_random(max_number):
    random_number = random.randint(0, max_number)
    return random_number


print(create_time())
print(output_local_time())
print(calculate_difference(3245453253452, 54453189))
print(generate_random(100))
