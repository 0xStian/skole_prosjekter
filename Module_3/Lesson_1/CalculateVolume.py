# Create a script called CalculateVolume.py. An engineer wants to calculate the volume of a rectangular tank using the formula length width height.
# The program needs to request these three values as input from the user and store them in three different variables. Using these three variables,
# calculate the volume of the tank and store it in a fourth variable.
# The engineer has learned from experience that measurements and calculations are always a bit short of the volume the tank can store because the plastic tank expands when filled.
# Therefore, he requires that the script increase the calculated volume of the tank by 1% before displaying the resulting volume to the user.


length = int(input("length: "))
width = int(input("width: "))
height = int(input("height: "))
volume = length * width * height
percentage = volume / 100
print(f"Real Volume = {volume + percentage}")