import math

while True:
    solvefor = input("What to solve for? a = Adjacent, o = Opposite: ").lower()

    if solvefor == "a":
        print("Adjacent length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            opposite = float(input("Opposite length? "))
            print(f"Opposite length is {opposite}\n")

            angle_radians = math.radians(angle)
            solveforadjacentresult = round(opposite / math.tan(angle_radians), 8)

            print(f"Adjacent length is {solveforadjacentresult}")
        except ValueError:
            print("Invalid input for angle and/or opposite")

        break

    elif solvefor == "o":
        print("Opposite length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            adjacent = float(input("Adjacent length? "))
            print(f"Adjacent length is {adjacent}\n")

            angle_radians = math.radians(angle)
            solveforoppositeresult = round(adjacent * math.tan(angle_radians), 8)

            print(f"Opposite length is {solveforoppositeresult}")
        except ValueError:
            print("Invalid input for angle and/or adjacent")

        break
    else:
        print("Not a valid choice\n")