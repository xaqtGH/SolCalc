import math

while True:
    try:
        number1 = float(input("1st number? "))
        number2 = float(input("2nd number? "))
        result = number1 / number2
        print(result)
    except ZeroDivisionError:
        print("rlly")