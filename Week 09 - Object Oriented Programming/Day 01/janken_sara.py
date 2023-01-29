import random

class Janken:


    def __init__(self):
        self.choices = ['rock', 'paper', 'scissors']
        self.player_wins = 0
        self.ai_wins = 0
        self.draws = 0
        self.total_games = 0
        self.playgame = self.playgame()

    def playgame(self):
        self.player_hand = input("Please choose between 'Rock', 'Paper' or 'Scissors: ").lower()
        ai_hand = random.choice(self.choices)
        if self.player_hand == 'rock':
            if ai_hand == 'rock':
                self.draws += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. It's a draw!")
            elif ai_hand == 'scissors':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. AI won!")
        elif self.player_hand == 'paper':
            if ai_hand == 'paper':
                self.draws += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. It's a draw!")
            elif ai_hand == 'rock':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. AI won!")
        elif self.player_hand == 'scissors':
            if ai_hand == 'scissors':
                self.draws += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. It's a draw!")
            elif ai_hand == 'paper':
                self.player_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. You won!")
            else:
                self.ai_wins += 1
                print(f"You chose {self.player_hand} and the AI chose {ai_hand}. AI won!")
        else:
            print(f"{self.player_hand} is a valid input. Please choose between 'Rock', 'Paper' or 'Scissors'.")
            return self.player_hand
            playgame()
        self.total_games += 1
        self.playagain()

    def playagain(self):
        new_game = input("Would you like to play again? (Y/N): ").lower()
        if new_game == 'y':
            self.playgame()
        else:
            self.get_results()
            print("Thanks for playing!")

    def get_results(self):
        print(f"You have played {self.total_games} matches against the AI.\nPLAYER WINS: {self.player_wins}\nAI WINS: {self.ai_wins}\nDRAWS: {self.draws}")

my_game = Janken()






