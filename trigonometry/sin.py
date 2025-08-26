import math

while True:
    solvefor = input("What to solve for? o = Opposite, h = Hypotenuse: ").lower()

    if solvefor == "o":
        print("Opposite length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            hypotenuse = float(input("Hypotenuse length? "))
            print(f"Hypotenuse length is {hypotenuse}\n")

            angle_radians = math.radians(angle)
            solveforoppositeresult = round(hypotenuse * math.sin(angle_radians), 8)

            print(f"Opposite length is {solveforoppositeresult}")
        except ValueError:
            print("Invalid input for angle and/or hypotenuse. Please enter numeric values.")

        break

    elif solvefor == "h":
        print("Hypotenuse length missing...\n")

        try:
            angle = float(input("Angle? (In degrees): "))
            print(f"Angle is {angle} degrees")

            opposite = float(input("Opposite length? "))
            print(f"Opposite length is {opposite}\n")

            angle_radians = math.radians(angle)
            solveforhypotenuseresult = round(opoosite / math.sin(angle_radians), 8)

            print(f"Opposite length is {solveforhypotenuseresult}")
        except ValueError:
            print("Invalid input for angle and/or opposite. Please enter numeric values.")

        break


    else:
        print("Not a valid choice\n")
