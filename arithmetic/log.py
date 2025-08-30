import math

while True:
    logtypechoice = input("Use natural logarithm ? (Y/N) ").lower()

    if logtypechoice == "y":
        natlognum = float(input("Enter a number "))
        natlognumresult = (math.log(natlognum))
        print(natlognumresult)
        

    elif logtypechoice == "n":
        base = float(input("Base? "))
        lognum = float(input("Number? "))
        logresult = math.log(lognum, base)
        print(logresult)

    else:
        print("srsly")