"""
Create a script called SummingMachine.py. In the script, create a function called summing_machine. The function should receive no argument. 
It should continously ask the user to enter a number until they enter a value to stop, e.g. 's'. 
The values entered must be added together and the final result returned to the calling code. 
Demonstrate the use of the function in the main section of your script.
'"""

def summing_machine():
    sum = 0
    while True:
        user_input = input("Enter numeric value ('e' to stop): ")
        if user_input == "e":
            return sum
        else:
            sum += int(user_input)
        

print(summing_machine())