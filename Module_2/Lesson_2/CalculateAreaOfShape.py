"""
Create a script called CalculateAreaOfShape.py. In the script, create a function called calculate_area_of_shape. The function should receive 5 arguments.
The first argument should define what shape's area needs to be calculated, e.g. "Square".
The other 4 arguments should be used to send measurements for length, height, width and radius. These 4 arguments should default to the value 0 if not used.
Your function should be able to calculate the area of at least 3 different shapes, e.g. square, cube and circle.
In the main section of your script, demonstrate the calculation of the area of 3 shapes. Your function calls should make use of named arguments.
"""


def calculate_area_of_shape(shape, length=0, height=0, width=0, radius=0):
    if shape == "square":
        surface_area = 2*(length*length + height*height + width*width)
        print(surface_area)
    elif shape == "circle":
        π = 3.14159
        area_of_circle = π * float(radius) * float(radius)
        print(area_of_circle) 
    else:
        print("invalid shape")
        
    
while True:
    shape = str(input("Shape (square, circle): ").lower())
    if shape == "square":
        length = int(input("Length: "))
        height = int(input("Height: "))
        width = int(input("Width: "))
        calculate_area_of_shape(shape, length, height, width) 
    elif shape == "circle":
        radius = input("Radius: ")
        calculate_area_of_shape(shape, 0, 0, 0, radius)
    else:
        print("invalid shape")
        pass
