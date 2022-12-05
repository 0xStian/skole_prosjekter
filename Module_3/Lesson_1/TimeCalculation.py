# Create a script called TimeCalculation.py. 
# A manager has requested that you write a script that allows him to enter a value representing the number of minutes one of his employees has worked in a month. 
# He wants the script to use the number of minutes to calculate the number of days worked in the month,
# the number of hours left over (not adding up to a full working day) and the number of minutes left over (not adding up to a full hour). For the sake of this calculation,
# a working day consists of eight hours. Once calculated, display the resulting calculation in the following format: working days:hours:minutes.

time = int(input("Minutes worked: "))
days = int(time / 1440)     
leftover_minutes = int(time % 1440)
hours = int(leftover_minutes / 60)
mins = int(time - (days*1440) - (hours*60))
print(f"working {days}:{hours}:{mins}")