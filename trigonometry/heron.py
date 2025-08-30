import math

while True:
    try:
        aparam = float(input("Side A?\n"))
        bparam = float(input("Side B? \n"))
        cparam = float(input("Side C? \n"))

        semiperimeter = (aparam + bparam + cparam) / 2

        area = math.sqrt(semiperimeter * (semiperimeter - aparam) * (semiperimeter - bparam) * (semiperimeter - cparam))

        print(f"Area is {area} u^2")

    except ValueError as e:
        print(f"Something doesn't seem possible here... {e}")