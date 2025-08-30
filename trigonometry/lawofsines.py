import math

while True:
    try:
        missinginfo = input("What's missing? [a] = Side A [b] = Side B [sina] = Sin Of A [sinb] = Sin Of B ").lower().strip()
        match missinginfo:
            case "a":
                sinofadeg = float(input("Angle of A? (degrees)\n"))
                sinofarad = math.radians(sinofadeg)
                sinofa = math.sin(sinofarad)
                print(f"Sin of A is {sinofa}")

                sinofbdeg = float(input("Angle of B? (degrees)\n"))
                sinofbrad = math.radians(sinofbdeg)
                sinofb = math.sin(sinofbrad)
                print(f"Sin of B is {sinofb}")

                blength = float(input("Length of B side? \n"))
                print(f"Length of B is {blength}")

                alength = round((sinofa * blength) / sinofb ,8)
                print(f"Length of A side is {alength}\n")

            case "b":
                alength = float(input("Length of A side? \n"))
                print(f"Length of A side is {alength}")

                sinofadeg = float(input("Angle of A? (degrees)\n"))
                sinofarad = math.radians(sinofadeg)
                sinofa = math.sin(sinofarad)
                print(f"Sin of A is {sinofa}")

                sinofbdeg = float(input("Angle of B? (degrees)\n"))
                sinofbrad = math.radians(sinofbdeg)
                sinofb = math.sin(sinofbrad)
                print(f"Sin of B is {sinofb}")

                blength = round((sinofb * alength) / sinofa, 8)

                print(f"Length of B side is {blength}")

            case "sina":
                alength = float(input("Length of A side? \n"))
                print(f"Length of A side is {alength}")

                blength = float(input("Length of B side? \n"))
                print(f"Length of B is {blength}")

                sinofbdeg = float(input("Angle of B? (degrees)\n"))
                sinofbrad = math.radians(sinofbdeg)
                sinofb = math.sin(sinofbrad)
                print(f"Sin B is {sinofbdeg}")

                sinofa = (alength * sinofb) / blength
                sinofarad = math.asin(sinofa)
                sinofadeg = round(math.degrees(sinofarad), 8)
                print(f"Angle A is {sinofadeg} degrees \n")

            case "sinb":
                alength = float(input("Length of A side? \n"))
                print(f"Length of A side is {alength}")

                blength = float(input("Length of B side? \n"))
                print(f"Length of B is {blength}")

                sinofadeg = float(input("Angle of A? (degrees)\n"))
                sinofarad = math.radians(sinofadeg)
                sinofa = round(math.sin(sinofarad), 8)
                print(f"Sin A is {sinofa}")

                sinofb = (sinofa * blength ) / alength
                sinofbrad = math.asin(sinofb)
                sinofbdeg = round(math.degrees(sinofbrad), 8)
                print(f"Angle B is {sinofbdeg} degrees \n")


    except ValueError:
        print("Invalid input, or one of the parameters are wrong")