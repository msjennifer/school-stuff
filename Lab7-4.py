#Jennifer Jones
#November 2, 2015
#Lab 7-4 Math Test Program

import random

#the main function
def main():
    #initialize variables
    counter = 0
    questions = 0
    userName = 'MISSING NAME'
    correct = 0
    averageCorrect = 0
    randomNumber1 = 0
    randomNumber2 = 0
#call to getUserName
    userName = getUserName()
    questions = getQuestionCount()
    #while loop to run program again
    while counter < questions:
        randomNumber1, randomNumber2 = getRandomNumbers()
        #askQuestion
        answer = askQuestion(randomNumber1, randomNumber2)
        #checkAnswer
        correct = checkAnswer(randomNumber1, randomNumber2, answer, correct)
        counter = counter + 1
    #function getStatistic
    averageCorrect = getStatistic(correct, averageCorrect, questions)
    #print average
    outputInfo(correct, averageCorrect, userName)

def getUserName():
    userName = raw_input('Enter user Name: ')
    return userName

def getQuestionCount():
    questions = input('How many math questions would you like to answer? ')
    return questions

def getRandomNumbers():
    randomNumber1 = random.randint(1, 99)
    randomNumber2 = random.randint(1, 99)
    return randomNumber1, randomNumber2

def askQuestion(randomNumber1, randomNumber2):
    print 'What is the answer to the following equation?'
    print randomNumber1
    print '*'
    print randomNumber2
    answer = input('What is the product: ')
    return answer

def checkAnswer(randomNumber1, randomNumber2, answer, correct):
    if answer == randomNumber1 * randomNumber2:
        print 'Right'
        correct = correct + 1
    else:
        print 'Wrong'
    return correct

def getStatistic(correct, averageCorrect, questions):
    averageCorrect = float(correct) / questions
    return averageCorrect

def outputInfo(correct, averageCorrect, userName):
    print
    print 'Information for user: ', userName
    print 'The number you answered correctly: ', correct
    print 'The average correct answer is: ', round(averageCorrect, 2), 'or', round(averageCorrect, 2) * 100,'%'
    


main()
