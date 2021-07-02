import random
import os
#from time import sleep
from twilio.rest import Client
from colorama import Fore, Back, Style



#function to clear the console
def clear():
    os.system('clear')

#function to send the message
def message(score):
    client = Client("ACc57459795cd42b520978ecf3b5413641", "32d4a914d0bbe4daeae97d9b282a99ac")
    client.messages.create(to=f"{phone_number}", 
                       from_="+15097403668", 
                       body="Your game score is"+str(score))

#the main funtion that hints the user for input
def hint():
    if int(number/2)*2==number:
        print("\nHint:")
        return print("The number is even")
        
    else:
        print("\nHint:")
        return print("The number is odd")



def get_user_guess():
    while True:
        try:
            guess=int(input("Enter your guess between 1 and 100 : "))
            diff=number-guess
            print("Difference between actual number and guess is :"+str(diff))
            print("You entered :"+str(guess))
            break
            
        except:
            print("Enter a valid number")
        
    
        
        
    
        
    
#function that does a repeat check if the user fails initial try
def repeat_check():
    if guess==number:
        print("\nYou got it right")
        print("Your score is  :"+str(score_repeat))
        message(score_repeat)
    else:
        print("\nYou got it wrong")
        print("Your score is  :" +str(score_fail))
    
#function that checks for the right score
def check():       
    if guess==number:
        print("Your score is :"+str(score_normal))
        message(score_normal)
        return True
    else:
        print("\nYou got it wrong")
        print("Try again")
        for i in range(1):
            multiple_check()
            hint()
            user_guess()
            repeat_check()
        return False
            
    

#function that checks for multiples of the number
def multiple_check():
    number_list=[]
    for  i in range(2,101):
        if number>=i and i==number:
            if number%i==0:
                number_list.append(i)
                
        elif i>=number:
            if i%number==0:
                number_list.append(i)
                
    print("""\nEXTRA HINT
        \nIt's multiples are """+str(number_list) )
        
      
                  
if __name__=="__main__":
    number=random.randrange(1,101)
    print(Back.LIGHTCYAN_EX+Fore.BLACK+"\n*********NUMBER_GUESSING_GAME*********"+Back.RESET+Fore.RESET)
    phone_number=str(input("Enter your Phone number: "))
    score_normal=10
    score_repeat=5
    score_fail=0
    hint()
    get_user_guess()
    check()
    