import math

while True:
    try:
        angleorside = input("What are you solving for? [a] = angle [s] = side ").lower()
        match angleorside:
            case "a":
                angletosolve = input("Which angle to solve? [a] = A [b] = B [c] = C ").lower()
                match angletosolve:
                    case "a":
                        alength = float(input("A side length? "))
                        print(f"Length of A side is {alength}")

                        blength = float(input("B side length? "))
                        print(f"Length of B side is {blength}")

                        clength = float(input("C side length? "))
                        print(f"Length of C side is {clength}")

                        anglea = round(math.acos(((blength**2) + (clength**2) - (alength**2)) / (2 * blength * clength)), 8)
                        angleadeg = math.degrees(anglea)
                        print(f"Angle A (Alpha) is {angleadeg} degrees")

                    case "b":
                        alength = float(input("A side length? "))
                        print(f"Length of A side is {alength}")

                        blength = float(input("B side length? "))
                        print(f"Length of B side is {blength}")

                        clength = float(input("C side length? "))
                        print(f"Length of C side is {clength}")

                        angleb = round(math.acos(((alength**2) + (clength**2) - (blength**2)) / (2 * alength * clength)), 8)
                        anglebdeg = math.degrees(angleb)
                        print(f"Angle B (Beta) is {anglebdeg} degrees")

                    case "c":
                        alength = float(input("A side length? "))
                        print(f"Length of A side is {alength}")

                        blength = float(input("B side length? "))
                        print(f"Length of B side is {blength}")

                        clength = float(input("C side length? "))
                        print(f"Length of C side is {clength}")

                        anglec = round(math.acos(((blength**2) + (alength**2) - (clength**2)) / (2 * alength * blength)), 8)
                        anglecdeg = math.degrees(anglec)
                        print(f"Angle C (Gamma) is {anglecdeg} degrees")

            case "s":
                sidetosolve = input("Which side to solve? [a] = A [b] = B [c] = C ").lower()
                match sidetosolve:
                    case "a":
                        blength = float(input(f"B side length? "))
                        print(f"B side length is {blength}")

                        clength = float(input(f"C side length? "))
                        print(f"C side length is {clength}")

                        aangle = float(input("Angle A (Alpha) in degrees? "))
                        print(f"Alpha angle is {aangle} degrees")
                        aanglerad = math.radians(aangle)

                        alength = round(math.sqrt((blength**2) + (clength **2) - 2*blength*clength * math.cos(aanglerad)), 8)
                        print(f"A side is {alength}")

                    case "b":
                        alength = float(input(f"A side length? "))
                        print(f"A side length is {alength}")

                        clength = float(input(f"C side length? "))
                        print(f"C side length is {clength}")

                        bangle = float(input("Angle B (Beta) in degrees? "))
                        print(f"Beta angle is {bangle} degrees")
                        banglerad = math.radians(bangle)

                        blength = round(math.sqrt((alength**2) + (clength **2) - 2*alength*clength * math.cos(banglerad)), 8)
                        print(f"B side is {blength}")

                    case "c":
                        alength = float(input(f"A side length? "))
                        print(f"A side length is {alength}")

                        blength = float(input(f"B side length? "))
                        print(f"B side length is {blength}")

                        cangle = float(input("Angle C (Gamma) in degrees? "))
                        print(f"Gamma angle is {cangle} degrees")
                        canglerad = math.radians(cangle)

                        clength = round(math.sqrt((alength**2) + (blength **2) - 2*alength*blength * math.cos(canglerad)), 8)
                        print(f"C side is {clength}")

    except ValueError:
        print("Invalid input, or an impossible triangle!")