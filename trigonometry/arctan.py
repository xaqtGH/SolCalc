import math

while True:
    try:
        opposite = float(input("Opposite length? "))
        print(f"Opposite is {opposite}\n")
        adjacent = float(input("Adjacent length? "))
        print(f"Adjacent is {adjacent}\n")

        angleresultradian =  math.atan(opposite/adjacent)
        angleresultdegrees = math.degrees(angleresultradian)

        print(f"Angle is {angleresultdegrees} degrees\n")

    except ValueError:
        print("Not a valid length for opposite and/or adjacent ")