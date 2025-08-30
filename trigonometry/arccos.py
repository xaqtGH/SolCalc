import math

while True:
    try:
        adjacent = float(input("Adjacent length? "))
        print(f"Adjacent is {adjacent}\n")
        hypotenuse = float(input("Hypotenuse length? "))
        print(f"Hypotenuse is {hypotenuse}\n")

        angleresultradian =  math.acos(adjacent/hypotenuse)
        angleresultdegrees = math.degrees(angleresultradian)

        print(f"Angle is {angleresultdegrees} degrees\n")

    except ValueError:
        print("Not a valid length for adjacent and/or hypotenuse ")