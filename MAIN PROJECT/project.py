import random
from twilio.rest import Client

score_normal=10
score_repeat=5
score_fail=0
number=random.randrange(0,10)

def message(score):
    #due to security reasons I can not expose my log in credentials
    client = Client("AC***********", "**********")
    client.messages.create(to="+2547*******", 
                       from_="+1********", 
                       body="Your game score is"+str(score))
    


def main():
    if int(number/2)*2==number:
        print("""Hints:
        The number is even""")
    else:
        print("""Hints:
        The number is odd""")
    global guess
    guess=int(input("\nEnter your Guess between 1 and 10: "))

    if number>guess:
        diff=number-guess
    else:
        diff=guess-number
    
    print("Difference between actual number and guess is : "+str(diff))
    

def repeat_check():
    if guess==number:
        print("\nYou got it right")
        print("Your score is  :"+str(score_repeat))
        message(score_repeat)
    else:
        print("\nYou got it wrong")
        print("Your score is  :" +str(score_fail))
    


def check():       
    if guess==number:
        print("Your score is "+str(score_normal))
        message(score_normal)
    else:
        print("\nYou got it wrong")
        print("Try again")
        for i in range(2):
            main()
            repeat_check()
            message(score_repeat)

        

main()
check()
    


    
