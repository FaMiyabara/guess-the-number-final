from art import logo
from random import randint

EASY_LEVEL = 10
HARD_LEVEL = 5

def check_answer(guess,number,turns):
  
  if guess == number:
    print(f"You win!!! The answer was {number}")

  elif guess>number:
    print("Too high.\n")
    return turns-1

  elif guess<number:
    print("Too low.\n")
    return turns-1

def difficulty():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  
  if difficulty == 'easy':
    return EASY_LEVEL
  else:
    return HARD_LEVEL


def game():    
  print (logo)
  number = randint(1,100)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  print (f"The correct answer is {number}")

  turns = difficulty()
  guess = 0  
  while guess != number:
    print(f"\nYou have {turns} attempts remaining to guess the number.")
    
    guess = int(input("Make a guess: "))

    turns = check_answer(guess,number,turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != number:
      print("Guess again.")
      
game()
    



    