#Name:  Stas Mironenko, Matt Keplinger
#Title: RSLPS
#File:  game.py
#Date:  12 Aug 2021

#imports
from human import Human
from computer import Computer

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = None

    def run_game(self):
        self.intro()
        self.rules()
        self.determine_game_type()
        self.create_round()
    
    def intro(self):
        print("\nWelcome to Paper, Rock, Scissors, Lizard, Spock")
        print(f'The game will be played in a "Best of 3" format\n')
        print(f'A tie will neither award or subtract points from either player')

    def rules(self):
        print("The rules are as follows:")
        print("Paper disproves Spock and covers Rock") 
        print("Rock crushes Scissors and Lizard")
        print("Scissors cuts Paper and decapitates Lizard")
        print("Lizard poisons Spock and eats Paper")
        print("Spock smashes Scissors and vaporizes Rock\n")

    def determine_game_type(self):
        game_choice = int(input(f'{self.player_one}, Select your opponent from the following:\n1-Computer\n2-Human Opponent\nYour Selection: '))
        if (game_choice == 1):
            self.player_two = Computer()
            print(f'Opponents confirmed: {self.player_one} vs. {self.player_two}')
        elif(game_choice == 2):
            self.player_two = Human()
            print(f'Opponents confirmed: {self.player_one} vs. {self.player_two}')
        else:
            self.determine_game_type()

    # player gesture must defeat other player gesture, while player has less than 2 of 3 wins
    # game is over when player has 2 wins
    def create_round(self):
        while (self.player_one.wins < 2 and self.player_two.wins < 2):
            p1_choice = self.player_one.choose_gesture()
            print(p1_choice)
            p2_choice = self.player_two.choose_gesture()
            print(p2_choice)
            self.round_winner(p1_choice, p2_choice)
        
        if (self.player_one.wins == 2 or self.player_two.wins == 2):
            self.overall_winner()

    def round_winner(self,p1_choice, p2_choice):
        if (p1_choice == p2_choice):
            print(f'Tie Game. No Points Awarded')
        elif(p1_choice == 1 and (p2_choice == 2 or p2_choice == 3)):
            print(f'{p1_choice} beats {p2_choice}')
            self.player_one.wins += 1
        elif(p1_choice == 2 and (p2_choice == 0 or p2_choice == 4)):
            print(f'{p1_choice} beats {p2_choice}')
            self.player_one.wins += 1
        elif(p1_choice == 3 and (p2_choice == 1 or p2_choice == 3)):
            print(f'{p1_choice} beats {p2_choice}')
            self.player_one.wins += 1
        elif(p1_choice == 4 and (p2_choice == 1 or p2_choice == 4)):
            print(f'{p1_choice} beats {p2_choice}')
            self.player_one.wins += 1
        elif(p1_choice == 5 and (p2_choice == 0 or p2_choice == 2)):
            print(f'{p1_choice} beats {p2_choice}')
            self.player_one.wins += 1
        else:
            print(f'{p2_choice} beat {p1_choice}')
            self.player_two.wins +=1

    #a player must have 2 wins to be declared winner
    def overall_winner(self):
        pass
