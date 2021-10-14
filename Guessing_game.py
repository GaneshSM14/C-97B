import random
Number=random.randint(1,9)
Chances=0
print("Guess a number between 1 to 9 ")
while Chances<5:
    Guess=int(input("ENTER YOUR GUESS"))
    if Guess==Number:
       print("YOU HAVE WON")
       break 
    elif Guess<Number:
        print("Your Guess is to low, Guess a number higher than ",Guess)

    else:
       print("Your Guess was to high, Guess a number lower than ", Guess)

Chances=Chances=+1
if not Chances<5:
    print("you lose the number is ",Number)
