# We need to import random to generate the questions
import random

# Give the player 3 lives and score AND how many questions asked
lives = 3
score = 0
ask = 0

# Loop for the game
while True:
    # Check if they are finished
    if lives == 0:
        print("GAME OVER")
        break
    elif ask == 10:
        print("YOU WIN!")
        print("You scored", score, "out of 10")
        break
    # The program picks a random number from 1 to 4, this will determine the type of
    # question to ask the user
    typeOfQuestion = random.randint(1,4)
    ask += 1
    print("Question", ask)
    # ASK one of the four types of questions
    if typeOfQuestion == 1:
        # Addition Question
        x = random.randint(1,12)
        y = random.randint(1,12)
        theAnswer = x + y
        print("What is",x,"+",y,"?")
        theirAnswer = int(input("> "))
    elif typeOfQuestion == 2:
        # Subtraction
        x = random.randint(1,12)
        y = random.randint(1,12)
        theAnswer = x - y
        print("What is",x,"-",y,"?")
        theirAnswer = int(input("> "))
    elif typeOfQuestion == 3:
        # Multiplication
        x = random.randint(1,12)
        y = random.randint(1,12)
        theAnswer = x * y
        print("What is",x,"*",y,"?")
        theirAnswer = int(input("> "))
    elif typeOfQuestion == 4:
        # Division
        x = random.randint(1,12)
        y = random.randint(1,12)
        z = x*y
        y = z/x
        theAnswer = y
        print("What is ",z,"/",x,"?")
        theirAnswer = int(input("> "))
    # Check if they are right or wrong
    if theAnswer == theirAnswer:
        print("CORRECT!")
        score += 1
    else:
        print("WRONG!")
        lives -= 1

# Quit the program
quit()
