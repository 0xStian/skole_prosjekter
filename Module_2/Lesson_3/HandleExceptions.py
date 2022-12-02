"""Create a script called HandleExceptions.py. In the script, create a section of code that requests sales numbers from a user.
The user should be able to enter as many sales values as they choose to. All sales values should always be entered as float values.
Each value entered should be added to a list of sales values. Provide a means for the user to stop entering sales values.
Once all the sales values have been entered, the user wants to be able to calculate the total of the sales figures,
but the user should be able to specifiy how many sales figures should be added to the total, i.e. if the user request that 5 sales figures should be added to the total,
the program should sum the first 5 values in the list. There are multiple places in this program where errors may occur. Ensure that any exceptions that do occur are handled.
"""

sales_numbers = []
while True:
    current_number = input("sales number ('stop' to stop): ")
    if current_number == "stop":
        number_to_sum = int(input("how many numbers should be summed: "))
        sum = 0.0
        if number_to_sum > 0 and number_to_sum <= len(sales_numbers):
            for x in sales_numbers[:number_to_sum]:
                sum += x
            print(f"sales sum = {sum}")
            quit()
        else:
            print("[!] Number to be summed is out of range!")
            pass
            
    else:
        try:
            sales_numbers.append(float(current_number))
        except ValueError:
            print("[!] Input is not a Float")