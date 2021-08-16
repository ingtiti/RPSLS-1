#Name:  Stas Mironenko, Matt Keplinger
#Title: RSLPS
#File:  computer.py
#Date:  12 Aug 2021

#imports
from player import Player
from random import choice

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.set_name()

    def set_name(self):
        self.name = "Computer"

    def choose_gesture(self):
        self.choice = choice(self.gesture_list)
        return self.choice

    def set_wins(self):
        self.wins += 1
        
    def __str__(self):
        return self.name
       