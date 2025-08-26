import math

while True:
    try:
        userinput = int(input("Type a decimal integer to convert to hexadecimal "))
        intuserinput = int(userinput)
        hexuserinput = hex(intuserinput)
        print(intuserinput,"in hex is",hexuserinput)
    except ValueError:
        print("Could not confirm, make sure to enter an integer")