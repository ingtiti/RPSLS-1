#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  player.py
#Date:  12 Aug 2021

class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        pass

    def choose_gesture(self):
        #method override for human and AI to choose gestures with appropriate logic for either
        pass

