while True:
    try:
        side = float(input("Side? \n"))
        area = side**2
        print(f"Area of the square is {area} u^2")
    
    except ValueError:
        print("Something went wrong")