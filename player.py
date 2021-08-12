#Name:  Stas Mironeko, Matt Keplinger
#Title: RSLPS
#File:  player.py
#Date:  12 Aug 2021

class Player:
    def __init__(self, name, wins):
        self.name = name
        self.wins = wins
        self.choose_gesture()
        self.gesture_list = ["rock", "paper", "scissors", "lizard", "spock"]
        pass

    def choose_gesture(self):
        pass

