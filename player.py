#Name:  Stas Mironenko, Matt Keplinger
#Title: RSLPS
#File:  player.py
#Date:  12 Aug 2021

class Player:
    def __init__(self):
        self.name = ''
        self.wins = 0
        self.gesture_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        self.choice = ''
        
    # Leave blank and override at Human, Computer 
    def choose_gesture(self):
        pass

