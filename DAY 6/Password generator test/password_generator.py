import random
import string

print("PASSWORD GENERATOR")


print("How strong do you want your password")
opt=int(input("Pick a  number(1,2,3) 1. Weak 2.Better 3.Stronger"))
    

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

if opt==1:
    passw=num+lower
    length=int(4)
elif opt==2:
    passw=num+upper+lower
    length=int(6)
elif opt==3:
    passw=lower+upper+num+symbols
    length=int(10)
else:
    print("Enter a valid option")

temp = random.sample(passw,length)
password = "".join(temp)

print("Your password is  "+ password)

