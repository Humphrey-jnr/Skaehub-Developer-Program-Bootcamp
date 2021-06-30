import random
import string


print("PASSWORD GENERATOR")

def main():
    print("How strong do you want your password")
    global opt
    opt=int(input("Pick a  number(1,2,3) 1. Weak 2.Better 3.Stronger : "))
    
    global lower
    lower = string.ascii_lowercase
    global upper
    upper = string.ascii_uppercase
    global num
    num = string.digits
    global symbols
    symbols = string.punctuation
    

    

    

    if opt==1:
        passw=num+lower
        length=int(4)
        global get_info
        print("weak password")
    elif opt==2:
        passw=num+upper+lower
        length=int(6)
        print(" moderate password")
    elif opt==3:
        passw=lower+upper+num+symbols
        length=int(10)
        print(" strong password")
    else:
        print("Enter a valid option")

    temp = random.sample(passw,length)
    global password
    password = "".join(temp)

    print("Your password is  "+ password)

main()


