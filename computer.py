#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  computer.py
#Date:  12 Aug 2021

#imports
from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()

    #set name, choose a gesture, set a score
    def set_name(self):
        self.name = "Computer"

    #override method from Player to use with random integer
    def choose_gesture(self):
        self.choice = self.gesture_list[random.randint(0.4)]

    def set_wins(self):
        self.wins += 1
