import random

play_again='yes'
while play_again=='yes':
    player=input('Rock, paper, or scissors?, type "r", "p", or "s" ')
    t=['r', 'p', 's']
    computer=random.choice(t)
    if player=='r' or player=='s' or player=='p':
        if computer=='r':
            print('Computer chose rock')
            if player=='p':
                print("You win!!!, paper covers rock")
            if player=='r':
                print('Its a draw')
            if player=='s':
                print('You lose :(, rock smashes scissors')    
        if computer=='p':  
            print('Computer chose paper')
            if player=='r':
                print('You lose :(, paper covers rock')
            if player=='p':
                print('Its a draw')
            if player=='s':
                print('You win!!!, scissors cut paper')
        if computer=='s':
            print('Computer chose scissors')
            if player=='r':
                print('You win!!!, rock smashes scissors')
            if player=='p':
                print('You lose :(, scissors cut paper')
            if player=='s':
                print('Its a draw')
        play_again=input('Do you want to play again?, yes or no ')
    else: 
        print('Please enter a valid input')
        play_again='yes'