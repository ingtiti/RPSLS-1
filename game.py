#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  game.py
#Date:  12 Aug 2021

#imports
from human import Human
from computer import Computer

class Game:
    def __init__(self):
        # pass
        self.player_one = Human()
        # self.player_two = None #undecided requires user input for AI or another human

    def run_game(self):
        self.intro()
        self.rules()
        pass
    
    def intro(self):
        print("\n\nWelcome to Paper, Rock, Scissors, Lizard, Spock")
        print(f'The game will be played in a "Best of 3" format\n')

    def rules(self):
        print("The rules are as follows:")
        print("Rock crushes Scissors")
        print("Scissors cuts Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitate Lizard")
        print("Lizard eats Paper")
        print("Paper disproves Spock")
        print("Spock vaporizes Rock")


    def determine_game_type(self):
        pass

    def determine_winner(self):
        pass
