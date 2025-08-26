import math

while True:
    try:
        userinput = int(input("Type a decimal integer to convert to binary "))
        intuserinput = int(userinput)
        binuserinput = bin(intuserinput)
        print(intuserinput,"in binary is",binuserinput)
    except ValueError:
        print("Could not confirm, make sure to enter an integer")