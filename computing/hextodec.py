try:
    hex_input = input("Input hex to convert to integer")
    decimal_value = int(hex_input, 16)
    print(f"The decimal equivalent of {hex_input} is: {decimal_value}")

except ValueError:
    print("Invalid")