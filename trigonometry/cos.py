import math

while True:
    solvefor = input("What to solve for? a = Adjacent, h = Hypotenuse: ").lower()

    if solvefor == "a":
        print("Adjacent length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            hypotenuse = float(input("Hypotenuse length? "))
            print(f"Hypotenuse length is {hypotenuse}\n")

            angle_radians = math.radians(angle)
            solveforadjacentresult = round(hypotenuse * math.cos(angle_radians), 8)

            print(f"Adjacent length is {solveforadjacentresult}")
        except ValueError:
            print("Invalid input for angle and/or hypotenuse")

        break

    elif solvefor == "h":
        print("Hypotenuse length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            opposite = float(input("Adjacent length? "))
            print(f"Adjacent length is {opposite}\n")

            angle_radians = math.radians(angle)
            solveforhypotenuseresult = round(opposite / math.cos(angle_radians), 8)

            print(f"Opposite length is {solveforhypotenuseresult}")
        except ValueError:
            print("Invalid input for angle and/or adjacent")

        break
    else:
        print("Not a valid choice\n")
