#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  computer.py
#Date:  12 Aug 2021

#imports
from player import Player
import random

class Computer(Player):
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.gesture = self.choose_gesture()

    def choose_gesture(self):
        choice = random.randint(0, len(self.gesture_list) - 1)
        action = self.gesture_list(choice)
        return action
        pass
