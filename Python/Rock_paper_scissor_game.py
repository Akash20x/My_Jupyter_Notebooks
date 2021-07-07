import random
game = 0
score1 = 0
score2 = 0

def random_move():
  choices = ['rock', 'paper', 'scissior']
  system_move = random.choice(choices)
  return system_move

def is_valid(user_move):
    move = user_move
    if (move == 'r'):
      move='rock'
    if (move == 'p'):
      move='paper'
    if (move == 's'):
      move='scissor'
    if (move == 'rock') or  (move == 'paper') or (move == 'scissior'):
      return move
    else:
      print('Please provide valid input.')

def result(move,system_move,score1,score2):
    if move == system_move:
        print(f"It's a tie round!")
    elif move == "rock":
        if system_move == "scissor":
            print("Rock smashed the scissors! You win this round!")
            score1 = score1 + 1
        else:
            print("Rock got covered by the Paper! You lose this round.")
            score2 = score2 + 1
    elif move == "paper":
        if system_move == "rock":
            print("Paper covered the rock! You win this round!")
            score1 = score1 + 1
        else:
            print("The Scissors cuts paper ! You lose this round.")
            score2 = score2 + 1
    elif move == "scissor":
        if system_move == "paper":
            print("Scissors cuts paper! You win this round!")
            score1 = score1 + 1
        else:
            print("Paper are smashed by Rock! You lose this round.")
            score2 = score2 + 1
    return score1 , score2

rounds = int(input("Enter no of rounds to play:"))
while game != rounds:
  print(f"\nRound {game+1}")
  user_move = str(input("Enter your move rock(r) or paper(p) or scissor(s): "))
  move = is_valid(user_move)
  system_move = random_move()
  print(f'The system chooses {system_move} where as you choose {user_move}!')
  score1, score2 = result(move,system_move,score1,score2)
  game= game + 1
  if game == rounds:
    print(f"\nUser wins {score1} rounds and system wins {score2} rounds")
    if score1<score2:
      print("System wins the game!")
    elif score1==score2:
      print("It's a tie!")
    else:
      print("User wins the game!")

