#Name:  Stas Mironenko, Matt Keplinger
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
        self.choice = int(input(f'\n{self.name}, Choose your move: \n1-rock\n2-paper\n3-scissors\n4-lizard\n5-spock\n\nYour Choice (enter #): '))
        if(self.choice == 1):
            return self.gesture_list[self.choice - 1]
        elif(self.choice == 2):
            return self.gesture_list[self.choice - 1]
        elif(self.choice == 3):
            return self.gesture_list[self.choice - 1]
        elif(self.choice == 4):
            return self.gesture_list[self.choice - 1]
        elif(self.choice == 5):
            return self.gesture_list[self.choice - 1]

    def set_wins(self):
        self.wins += 1

    def __str__(self):
        return self.name