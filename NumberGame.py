import random 
import sys
Random_Number = random.randint(0, 1000)

print("Hello, would you like to play a game?")
answer = input()
if answer == "Yes" or "yes" or "y": 
    print("Awesome! I'm thinking of a number between 1 and 1000. You get 5 guesses.")
    print("What is your guess?")
    guess = 0
    while guess < 10:
        Number_Answer = int(input())

        if  Number_Answer > Random_Number:
            print("That number is too high, guess again!")
            guess += 1
        elif Number_Answer < Random_Number:
            print("that number is too low, guess again!")
            guess += 1
        else: 
            print("Congrats! You guess the number!")
            sys.exit()

    if guess == 10:
        print("Sorry, you didn't guess the number. The correct answer is " + str(Random_Number))
        sys.exit()
elif answer == "No" or "no" or "n":
    print("Ok, maybe another time!")
    sys.exit()