import math

while True:
    try:
        radius = float(input("Radius? \n"))
        area = round((math.pi * (radius**2)), 8)
        print(f"Area of the circle is {area} u^2")
    
    except ValueError:
        print("Invalid")
