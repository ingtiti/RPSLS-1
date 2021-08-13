#Name:  Stas Mironenko, Matt Keplinger
#Title: RSLPS
#File:  computer.py
#Date:  12 Aug 2021

#imports
from player import Player
import random

class Computer(Player):
    def __init__(self):
        super().__init__()
        self.set_name()

    #set name, choose a gesture, set a score
    def set_name(self):
        self.name = "Computer"

    #override method from Player to use with random integer
    def choose_gesture(self):
        self.choice = random.randint(0, len(self.gesture_list)-1)
        if(self.choice == 0):
            return 'Rock'
        elif(self.choice == 1):
            return 'Paper'
        elif(self.choice == 2):
            return 'Scissors'
        elif(self.choice == 3):
            return 'Lizard'
        elif(self.choice == 4):
            return 'Spock'

    def set_wins(self):
        self.wins += 1
        
    def __str__(self):
        return self.name
       