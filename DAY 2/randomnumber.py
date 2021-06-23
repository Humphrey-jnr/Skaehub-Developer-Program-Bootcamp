import random

def random_num():
    number=random.randrange(1, 10)
    guess=int(input("Enter guess between 1-10: "))

    if guess==number:
        print("GUess is right")
    else:
        print("Guess is wrong")
        random_num()

random_num()
