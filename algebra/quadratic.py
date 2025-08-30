import math, cmath

while True:
    try:
        a = float(input("\nA? \n"))
        print(f"A = {a}")

        b = float(input("B? \n"))
        print(f"B = {b}")

        c = float(input("C? \n"))
        print(f"C = {c}")

        if a == 0:
            print("A can't be 0")
            continue

        discrim = (b ** 2) - (4 * a * c)

        if discrim > 0:
            x1 = (-b + math.sqrt(discrim)) / (2 * a)
            x2 = (-b - math.sqrt(discrim)) / (2 * a)
            print("")
            print(f"X1 = {x1}")
            print(f"X2 = {x2}")

        elif discrim == 0:
            x = (-b) / (2 * a)
            print(f"X = {x}")

        else:
            x1 = (-b + cmath.sqrt(discrim)) / (2 * a)
            x2 = (-b - cmath.sqrt(discrim)) / (2 * a)
            print(f"X1 = {x1}")
            print(f"X2 = {x2}")

    except ValueError:
        print("Invalid")