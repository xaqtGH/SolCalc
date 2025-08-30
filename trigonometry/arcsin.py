import math

while True:
    try:
        opposite = float(input("Opposite length? "))
        print(f"Opposite is {opposite}\n")
        hypotenuse = float(input("Hypotenuse length? "))
        print(f"Hypotenuse is {hypotenuse}\n")

        angleresultradian =  math.asin(opposite/hypotenuse)
        angleresultdegrees = math.degrees(angleresultradian)

        print(f"Angle is {angleresultdegrees} degrees\n")

    except ValueError:
        print("Not a valid length for opposite and/or hypotenuse ")