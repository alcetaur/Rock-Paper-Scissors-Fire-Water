import random, sys

print('ROCK, PAPER, SCISSORS, FIRE, WATER')

# These variables keep track of the number of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: # The player input loop.
        print('To play, enter your move: rock,paper,scissors,fire,water')
        print('To quit, enter (quit)')
        playerMove = input()
        if playerMove == 'quit':
            sys.exit() # Quit the program.
        if playerMove == 'rock' or playerMove == 'paper' or playerMove == 'scissors' or playerMove == 'fire' or playerMove == 'water':
            break # Break out of the player input loop.
        print('Type one of the weapons!')

    # Display what the player chose:
    if playerMove == 'rock':
        print('You chose ROCK! ')
    elif playerMove == 'paper':
        print('PAPER vs')
    elif playerMove == 'scissors':
        print('SCISSORS vs')
    elif playerMove == 'fire':
        print('FIRE vs')
    elif playerMove == 'water':
        print('WATER vs')
    # Display what the computer chose:
    randomNumber = random.randint(1, 5)
    if randomNumber == 1:
        computerMove = 'rock'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'paper'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 'scissors'
        print('SCISSORS')
    elif randomNumber == 4:
        computerMove = 'fire'
        print('WATER')
    elif randomNumber == 5:
        computerMove = 'water'
        print('WATER')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print('It is a tie!')
        ties = ties + 1
    elif playerMove == 'rock' and computerMove == 'scissors':
        print('Rock beats scissors')
        wins = wins + 1
    elif playerMove == 'rock' and computerMove == 'water':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'paper' and computerMove == 'rock':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'paper' and computerMove == 'water':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'scissors' and computerMove == 'paper':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'scissors' and computerMove == 'water':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'fire' and computerMove == 'scissors':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'fire' and computerMove == 'rock':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'fire' and computerMove == 'paper':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'water' and computerMove == 'fire':
        print('You win!')
        wins = wins + 1
    elif playerMove == 'rock' and computerMove == 'paper':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'rock' and computerMove == 'fire':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'paper' and computerMove == 'scissors':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'paper' and computerMove == 'fire':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'scissors' and computerMove == 'rock':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'scissors' and computerMove == 'fire':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'water' and computerMove == 'rock':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'water' and computerMove == 'scissors':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'water' and computerMove == 'paper':
        print('You lose!')
        losses = losses + 1
    elif playerMove == 'fire' and computerMove == 'water':
        print('You lose!')
        losses = losses + 1