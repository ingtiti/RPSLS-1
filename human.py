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
    
    def set_player_name(self):
        self.name = input('\nHello, Player.  Please Enter your name:\n')

    def choose_gesture(self):
        self.choice = int(input(f'\n{self.name}, Choose your move: \n1-rock\n2-paper\n3-scissors\n4-lizard\n5-spock\nYour Choice (enter the digit next to your choice): '))
        allowed_nums = [1,2,3,4,5]
        if self.choice in allowed_nums:
                return self.gesture_list[self.choice - 1]
        else:
            self.choose_gesture()

    def set_wins(self):
        self.wins += 1

    def __str__(self):
        return self.name