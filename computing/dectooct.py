import math

while True:
    try:
        userinput = int(input("Type a decimal integer to convert to octal "))
        intuserinput = int(userinput)
        octuserinput = oct(intuserinput)
        print(intuserinput,"in octal is",octuserinput)
    except ValueError:
        print("Could not confirm, make sure to enter an integer")