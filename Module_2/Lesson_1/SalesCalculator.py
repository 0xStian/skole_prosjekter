"""
Create a script called SalesCalculator.py. The script should request 10 sales values from the user using a loop.
If the value entered by the user is less than 5000 the rest of the current loop iteration should not be performed.
If the value is higher than 5000 and less than 10001 the current sales total and sales average of the user should be printed to screen.
If the value is higher than 10000, the loop should stop entirely and a message should be displayed that a possible data entry error has occurred.
"""
sales = []
number_of_sales = 10
user_input = 0

for x in range(number_of_sales):
    user_input = int(input("Sales Value: "))
    if user_input < 5000:
        break
    
    elif user_input > 5000 and user_input < 10001:
        sales.append(user_input)
        print(f"total sales average {sum(sales) / len(sales)}")
        print(f"total sales sum {sum(sales)}")
        sum(sales)
           
    elif user_input > 10000:
        print("possible data entry error has occurred.")