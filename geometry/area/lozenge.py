while True:
    try:
        diagonal1 = float(input("Diagonal 1?\n"))
        diagonal2 = float(input("Diagonal 2? \n"))
        area = round((base * height)/2, 8)
        print(f"Area of the lozenge is {area} u^2")

    except ValueError:
        print("Something went wrong")