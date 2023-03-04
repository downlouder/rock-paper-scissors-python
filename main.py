import random

items = ['rock', 'paper', 'scissors']
answers = ['y', 'n']

def play():
    scores = 0
    computerScores = 0
    while scores < 5 and computerScores < 5:
        player = None
        while player not in items:
            player = input('Enter a choice (rock, paper, scissors): ')
            computer = random.choice(items)
            if player not in items: 
                print('Please, enter correct word')
        print(f"Player choice: {player}")
        print(f"Computer choice: {computer}")
        if player == computer:
            print('Tie nobody won or lost')
        elif (player == 'rock' and computer == 'scissors') or (player == 'paper' and computer == 'rock') or (player == 'scissors' and computer == 'paper'):
            scores += 1
            print('You won this round')
        else:
            computerScores += 1
            print('Computer won this round')
        print(f"Player scores: {scores} vs Computer scores: {computerScores}")
        player = None
        if scores >= 5:
            print('You won this game')
            again()
        elif computerScores >= 5:
            print('Computer won this game')
            again()

def again():
    answer = None
    while answer not in answers:
        answer = input('Do you want to play again?\nEnter "y" or "n": ')
        if answer == 'y':
            print('Good!!!')
            play()
        elif answer == 'n':
            print('See you later')

play()