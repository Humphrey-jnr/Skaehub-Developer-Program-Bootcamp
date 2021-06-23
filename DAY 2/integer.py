from math import log, floor
 
 
# Returns true if `n` is a power of four
def power_of_four(n):
 
    # find `log4(n)`
    i = log(n) / log(4)
    return i == floor(i)
 
 
def main():
 
    n = int(input("Enter n: "))
 
    if power_of_four(n):
        print(n, "is a power of 4")
    else:
        print(n, "is not a power of 4")


main()