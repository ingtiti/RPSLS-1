#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  game.py
#Date:  12 Aug 2021

#imports
from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Human().set_player_name
        self.player_two = None

    def run_game(self):
        self.intro()
        self.rules()
        self.determine_game_type()
    
    def intro(self):
        print("\n\nWelcome to Paper, Rock, Scissors, Lizard, Spock")
        print(f'The game will be played in a "Best of 3" format\n')

    def rules(self):
        print("The rules are as follows:")
        print("Paper disproves Spock and covers Rock") 
        print("Rock crushes Scissors and Lizard")
        print("Scissors cuts Paper and decapitates Lizard")
        print("Lizard poisons Spock and eats Paper")
        print("Spock smashes Scissors and vaporizes Rock")

    def determine_game_type(self):
        game_choice = int(input("Enter 1 for a game against the Computer, 2 for a game against a second human"))
        if (game_choice == 1):
            self.player_two = Computer()
        elif(game_choice == 2):
            self.player_two = Human()
        else:
            self.determine_game_type()

    def determine_winner(self):
        pass
