import random

def main():
    print_header()

    rolls = build_the_three_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)

    if player1.score > player2.score:
        print('Congratulations, you won!')
    else:
        print('You lose, bitch!')


def game_loop(player1, player2, rolls):
    while player1.score < 2 and player2.score < 2:

        inp = input('[R]ock, [P]aper or [S]cissors? ')
        if inp == 'R' or inp == 'r':
            p1_roll = rolls[0]
        elif inp == 'P' or inp == 'p':
            p1_roll = rolls[1]
        elif inp == 'S' or inp == 's':
            p1_roll = rolls[2]
        else:
            continue

        p2_roll = random.choice(rolls)

        if p1_roll.can_defeat == p2_roll.name:
            player1.score += 1
        elif p2_roll.can_defeat == p1_roll.name:
            player2.score += 1
        else:
            print('You tied, try again!')

        print('You played a', p1_roll.name)
        print('The computer played a', p2_roll.name)
        print('Your score:', player1.score, 'The computer:', player2.score)


def print_header():
    print('Welcome!')

class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0

def get_players_name():
    name = input('Please enter your name: ')
    return name

class Roll():
    def __init__(self, name, can_defeat):
        self.name = name
        self.can_defeat = can_defeat

def build_the_three_rolls():
    rolls = []
    rolls.append(Roll('rock', 'scissors'))
    rolls.append(Roll('paper', 'rock'))
    rolls.append(Roll('scissors', 'paper'))
    return rolls

if __name__ == '__main__':
    main()
