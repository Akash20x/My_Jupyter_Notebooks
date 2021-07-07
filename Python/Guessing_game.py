import random
game = False
player_score = 0


def player_guess(player_score,range_start,range_end):
    guess = 0
    random_no = random.randint(range_start, range_end)
    print("Computer generates a random number for a player to guess")
    while guess != random_no:
        guess = int(input(f'Guess a number between {range_start} and {range_end}: '))
        if guess > range_start and guess <= range_end:
          if guess < random_no:
              print("Try Again! You guessed too small")
              player_score = player_score + 1
          elif guess > random_no:
              print("Try Again! You guessed too high")
              player_score = player_score + 1
          elif guess == random_no:
              print(f"You guessed correctly, the number is {guess}")
              player_score = player_score + 1
              return player_score           
        else:
          print("Try Again! Number is not found in range\n")


while game != True:
    print("\nGuessing Game")
    range_start=int(input("Enter Starting Range:"))
    range_end=int(input("Enter Ending Range:"))
    if range_start < range_end:
      total_guess = player_guess(player_score,range_start,range_end)
      print(f"Total Number of Guesses = {total_guess}")
      response = input("Thanks for playing.  Play again? (y/n) :")
      if response == 'y':
          game = False
      elif response == 'n':
          game = True
          print("Bye..")
    else:
      print("Try Again! Choose range correctly\n")
