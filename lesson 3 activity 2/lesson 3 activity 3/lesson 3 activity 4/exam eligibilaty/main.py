num =int(input("enter number of marks"))
if num<50:
    print("F")
elif num>50:
    print("B+")
if num<60:
    print("-A")
elif num>70:
    print("A+")
elif num>99:
    print("GOLDEN A+")
if num>100:
    print("invalid input")