#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  human.py
#Date:  12 Aug 2021

#imports
from player import Player

class Human(Player):
    def __init__(self, gesture): 
        self.choose_gesture = gesture
        pass

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

        pass