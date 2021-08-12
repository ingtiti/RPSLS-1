#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  game.py
#Date:  12 Aug 2021

#imports
from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None #undecided requires user input for AI or another human

    def run_game(self):
        pass

    def determine_game_type(self):
        pass

    def determine_winner(self):
        pass
