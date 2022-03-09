# Student Number
import random

# This sets the score to 0 and the number of lives to 3
lives = 3
score = 0


# This is a for loop, at most ask 10 questions but game over if 3 are answered wrongly
for questionNumber in range(1,11):
    # Prints the question number
    print("Question", questionNumber)
    # Chooses a random question, 1 from 4 types
    questionType = random.randint(1,4)
    # If they have no life left, game over and BREAK OUT OF FOR
    if lives <= 0:
        print("OUT OF LIFE! GAME OVER!")
        break
    # + question
    elif questionType == 1:
        x = random.randint(1,12)
        y = random.randint(1,12)
        rightAnswer = x + y
        print("What is", x, "+", y, "?")
        theirAnswer = int(input("> "))
        if theirAnswer == rightAnswer:
            print("CORRECT!")
            score += 1
        else:
            print("WRONG!")
            lives -= 1
    # - question
    elif questionType == 2:
        x = random.randint(6,12)
        y = random.randint(1,5)
        rightAnswer = x - y
        print("What is", x, "-", y, "?")
        theirAnswer = int(input("> "))
        if theirAnswer == rightAnswer:
            print("CORRECT!")
            score += 1
        else:
            print("WRONG!")
            lives -= 1
    # * question
    elif questionType == 3:
        x = random.randint(1,12)
        y = random.randint(1,12)
        rightAnswer = x * y
        print("What is", x, "*", y, "?")
        theirAnswer = int(input("> "))
        if theirAnswer == rightAnswer:
            print("CORRECT!")
            score += 1
        else:
            print("WRONG!")
            lives -= 1
    # / question
    elif questionType == 4:
        k = random.randint(1, 12)
        y = random.randint(1, 12)
        x = k * y
        rightAnswer = x / y
        print("What is", x, "/", y, "?")
        theirAnswer = int(input("> "))
        if theirAnswer == rightAnswer:
            print("CORRECT!")
            score += 1
        else:
            print("WRONG!")
            lives -= 1

# Summary of score
print("Your score is", score, "out of 10.")

# Quit
quit()
