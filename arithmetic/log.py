import math

while True:
    logtypechoice = input("Use natural logarithm ? (Y/N) ")

    if logtypechoice == "Y":
        natlognum = float(input("Enter a number "))
        natlognumresult = (math.log(natlognum))
        print(natlognumresult)
        

    elif logtypechoice == "N":
        base = float(input("Base? "))
        lognum = float(input("Number? "))
        logresult = math.log(lognum, base)
        print(logresult)

    else:
        print("srsly")