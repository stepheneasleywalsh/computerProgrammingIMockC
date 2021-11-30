# Student Number 0000000
# Import random (needed to make the questions)
import random

# Start off with 3 lives
lives = 3

# Start with question n=1
n = 1

# Ask 10 questions only
for n in range(1,11):
    # print the question number
    print("Question",n)
    type = random.randint(1, 4)
    if lives == 0: # CHECKS IF GAME IS OVER
        print("GAME OVER!!!!!")
        quit()
    elif type == 1: # CHECKS if it is a + question
        x = random.randint(1,12)
        y = random.randint(1,12)
        print("What is",x,"+",y,"?")
        z = int(input("> "))
        if z == x+y:
            print("CORRECT!")
        else:
            print("WRONG!")
            lives -= 1
    elif type == 2: # CHECKS if it is a - question
        x = random.randint(1,12)
        y = random.randint(1,12)
        print("What is",x,"-",y,"?")
        z = int(input("> "))
        if z == x-y:
            print("CORRECT!")
        else:
            print("WRONG!")
            lives -= 1
    elif type == 3: # CHECKS if it is a * question
        x = random.randint(1,12)
        y = random.randint(1,12)
        print("What is",x,"*",y,"?")
        z = int(input("> "))
        if z == x * y:
            print("CORRECT!")
        else:
            print("WRONG!")
            lives -= 1
    elif type == 4: # CHECKS if it is a / question
        y = random.randint(1, 12)
        x = y*random.randint(1,12) ## This makes sure x/y is an integer
        print("What is",x,"/",y,"?")
        z = int(input("> "))
        if z == x / y:
            print("CORRECT!")
        else:
            print("WRONG!")
            lives -= 1

# WIN SCREEN
print("YOU WIN!")

# Score
score = 7 + lives
print("Your score is", score, "out of 10.")

# QUIT
quit()