import math

def perfect_square():
    num=int(input("Enter number: "))

    root=math.sqrt(num)

    if int(root)**2==num:
        print(num, " is a perfect square")
    else:
        print(num," is not a perfect square")


perfect_square()