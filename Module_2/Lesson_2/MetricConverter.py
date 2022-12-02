"""
Create a script called MetricConverter.py. In the script, create a function called metric_converter, which receives a single numeric argument.
The purpose of this method is to receive a value in inches and then convert it to centimetres.
The function should display on screen what the number of inches were that it received, as well as the number of centimetres after conversion.
The function should not return any values. Demonstrate the use of the function in the main section of your script.
"""

def metric_converter(x):
    print(f"{x * 2.54}cm")


while True: 
    metric_converter(float(input("Inches to Centimetres: ")))