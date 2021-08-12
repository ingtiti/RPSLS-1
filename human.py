#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  human.py
#Date:  12 Aug 2021

#imports
from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()
        self.set_player_name()
    
    #set name, choose a gesture, set a score
    def set_player_name(self):
        self.name = input('\nHello, Player.  Please Enter your name:\n')

    #fix this. use integers for easier validation instead of words
    def choose_gesture(self):
        user_choice = input("Choose your move: \npaper\nrock\nscissors\nlizard\nspock")
        if(user_choice == 'paper'):
            gesture = user_choice
        elif(user_choice == 'rock'):
            gesture = user_choice
        elif(user_choice == 'scissors'):
            gesture = user_choice
        elif(user_choice == 'lizard'):
            gesture = user_choice
        elif(user_choice == 'spock'):
            gesture = user_choice
        else:
            self.choose_gesture()

    def set_wins(self):
        self.wins += 1

    def __str__(self):
        return self.name