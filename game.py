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
        print('\nWelcome to Paper, Rock, Scissors, Lizard, Spock')
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
        game_choice = int(input(f'{self.player_one}, Enter the number to choose your opponent:\n1-Computer\n2-Human Opponent\nYour Selection: '))
        allowed_nums = [1,2]
        if game_choice in allowed_nums:
            if (game_choice == 1):
                self.player_two = Computer()
                print(f'Opponents confirmed: {self.player_one} vs. {self.player_two}')
            elif(game_choice == 2):
                self.player_two = Human()
                print(f'Opponents confirmed: {self.player_one} vs. {self.player_two}')
        else:
            self.determine_game_type()

    #creates a round of gameplay and keeps best of three format
    def create_round(self):
        while (self.player_one.wins < 2 and self.player_two.wins < 2):
            p1_choice = self.player_one.choose_gesture()
            p2_choice = self.player_two.choose_gesture()
            print(f'\n{self.player_one} chooses {p1_choice}')
            print(f'{self.player_two} chooses {p2_choice}')
            self.round_winner(p1_choice, p2_choice)
        
        if (self.player_one.wins == 2 or self.player_two.wins == 2):
            self.overall_winner()

    #determine who wins based on input, calls _wins method for winner (p1 or p2)
    def round_winner(self,p1_choice, p2_choice):
        if (p1_choice == p2_choice):
            print(f'Tie Game. No Points Awarded')
        elif(p1_choice == "Rock" and (p2_choice == "Scissors" or p2_choice == "Lizard")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Paper" and (p2_choice == "Rock" or p2_choice == "Spock")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Scissors" and (p2_choice == "Paper" or p2_choice == "Lizard")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Lizard" and (p2_choice == "Paper" or p2_choice == "Spock")):
            self.p1_wins(p1_choice, p2_choice)
        elif(p1_choice == "Spock" and (p2_choice == "Rock" or p2_choice == "Scissors")):
            self.p1_wins(p1_choice, p2_choice)
        else:
            self.p2_wins(p1_choice, p2_choice)
            
    def p1_wins(self, p1_choice, p2_choice):
        print(f'{p1_choice} beats {p2_choice}. {self.player_one} wins this round')
        self.player_one.set_wins()
    
    def p2_wins(self, p1_choice, p2_choice):
        print(f'{p2_choice} beats {p1_choice}. {self.player_two} wins this round!')
        self.player_two.set_wins()

    def overall_winner(self):
        if(self.player_one.wins == 2):
            print(f'{self.player_one} wins the game!')
        else:
            print(f'{self.player_two} wins the game!')
