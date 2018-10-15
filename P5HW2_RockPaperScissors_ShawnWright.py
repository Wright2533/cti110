# Rock, Paper Scissors Game
# 9/29/18
# CTI-110 P5HW2 - Rock, Paper, Scissors Game
# Shawn Wright
#

import random

# Generate a random numeber from 1 to 3
def generateRandomNumber():
    randomNumber = random.randint(1,3)
    return randomNumber

# The random number 1 is rock, 2 is paper, 3 is scissors
def getComputerChoice( randomNumber ):
    if randomNumber == 1:
        computerChoice = "rock"
    elif randomNumber == 2:
        computerChoice = "paper"
    elif randomNumber == 3:
        ComputerChoice = "scissors"

# Computer choice: either rock papaer or scissors
    return computerChoice


def getUserChoice():
    userChoice = input( "Please enter your choice: ")
    return userChoice

# determining the winner and forming winner messages for the winner
def determineWinner( computerChoice, userChoice ):
    rockMessage = "The rock smashes the scissors"
    scissorMessage = "Scissors cut paper"
    paperMessage = "Paper wraps rock"

    if computerChoice == "rock" and userChoice == "scissors":
        winner = "Computer"
        message = rockMessage
    elif computerChoice == "scissors" and userChoice == "rock":
            winner = "You"
            message = rockMessage

    if computerChoice == "scissors" and userChoice == "paper":
            winner = "Computer"
            message = scissorMessage
    elif computerChoice == "paper" and userChoice == "scissors":
            winner = "You"
            message = scissorMessage


    if computerChoice == "paper" and userChoice == "rock":
            winner = "computer"
            message = paperMessage
    elif computerChoice == "rock" and userChoice == "paper":
            winner = "You"
            message = paperMessage

    return  winner, message

# Main Function
def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice( randomNumber )
    userChoice = getUserChoice()
    
    print( "The computer chose", computerChoice )
    winner, message = determineWinner( computerChoice, userChoice )

    if winner != "no winner":
        print( winner, "won(", message, ")" )

    return winner

def main():
    randomNumber = generateRandomNumber()
    computerChoice = getComputerChoice( randomNumber )
    userChoice = getUserChoice()
    print()
    print( "The computer chose", computerChoice )
    winner, message = determineWinner( computerChoice, userChoice )

    if winner != "no winner":
        print( winner, "won(", message, ")" )

    while winner == "no winner":
        winner = startAgain()

main()
            
