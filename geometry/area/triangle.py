while True:
    try:
        base = float(input("Base?\n"))
        height = float(input("Height? \n"))
        area = round((base * height)/2, 8)
        print(f"Area of the triangle is {area} u^2")

    except ValueError:
        print("Something went wrong")