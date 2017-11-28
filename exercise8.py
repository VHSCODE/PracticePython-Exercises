"""
Random is used to generate a random integer between 1 and 3
"""
import random
userResponse = input("Paper, Rock or Scissors ?")

def generateComputerResponse():
    """
    This function creates and returns the computers choice
    """
    computerResponse= ""
    rand_numb = random.randint(1,3)
    if rand_numb == 1:
        computerResponse = "paper"
    elif rand_numb == 2:
        computerResponse = "rock"
    else:
        computerResponse = "scissors"
    
    return computerResponse


def decideWinner(user, computer):
    """
    This function determines the winner of the match and also if there is a draw
    """
    print("Computer has chosed" + " " + computer + "!")
    if user == computer:
        print("A draw !")
    
    elif user == "paper":
        if computer == "rock":
            print("User Wins !")
        else:
            print("Computer Wins !")
    
    elif user == "rock":
        if computer == "paper":
            print("Computer Wins !")
        
        else:
            print("User Wins !")
    
    else:
        if computer == "rock":
            print("Computer Wins !")
        else:
            print("User Wins !")

decideWinner(userResponse, generateComputerResponse())


