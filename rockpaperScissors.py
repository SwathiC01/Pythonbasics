import random
import sys

class RPS:
    def __init__(self):
        print("Welcome to RPS 9000!")
        self.valid_moves: list[str]=['rock','paper','scissors']

    def play_game(self):
        user_move: str = input("Rock, Paper or Scissors? ").lower()
        if user_move == 'exit':
            sys.exit()

        if user_move not in self.valid_moves:
            print("Invalid move....")
            return self.play_game()
        
        ai_move = random.choice(self.valid_moves)

        self.display_moves(user_move, ai_move)
        self.check_move(user_move, ai_move)

    def display_moves(self, user_move, ai_move):
        print('-------')
        print(f"You: {user_move}")
        print(f"AI: {ai_move}")
        print('-------')

    def check_move(self, user_move, ai_move):
        user_wins=0
        ai_wins=0
        if user_move==ai_move:
            print("Its a tie!!")
        elif user_move=='rock' and ai_move=='scissors':
            print("You win!")
            user_wins+=1
        elif user_move=='scissors' and ai_move=='paper':
            print("You win!")
            user_wins+=1
        elif user_move=='paper' and ai_move=='rock':
            print("You win!")
            user_wins+=1
        else:
            print("AI win")
            ai_wins+=1


if __name__== '__main__':
    rps=RPS()

    while True:
        rps.play_game()