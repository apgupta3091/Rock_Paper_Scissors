#Anuj Gupta
#Rock Paper Scissors game
#imports random
import random

user = None
computer = random.choice(['rock', 'paper', 'scissor'])
# Start of the while loop since user = None
while user == None:
    user = input('please enter the value you wish to choose:')
    # Error proofing the selction made by the user with an if not statement
    if user not in ['rock', 'paper', 'scissor']:
        print ('You need to choose the valid value and enter it in lower case letters')
        user = None

# prints who won the round based on the selections made by the user and the computer through if statements
# user == computer
if user == computer:
    print("Draw")
    
#user == rock    
if user == 'rock':
    if computer == 'paper':
        print ('computer wins')
    elif computer == 'scissor':
        print('user wins')
        
#user == paper        
if user == 'paper':
    if computer =='scissor':
        print('computer wins')
    elif computer == 'rock':
        print('user wins')
        
#user == scissor       
if user == 'scissor':
    if computer == 'rock':
        print ('computer wins')
    elif computer == 'paper':
        print('user wins')
        
# print the selections made by the computer and the user
print ('computer is {}'.format(computer))
print('user is {}'.format(user))
        

    
