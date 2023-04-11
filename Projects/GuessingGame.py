#STILL INCOMPLETE NEED TO CONTINUE WORKING
import random

print("Welcome to the guessing name!")
print("Im thining of a number between 1 and 100")

random_number = random.randint(1, 100)
print(random_number)
hard_difficulty = 5
easy_difficulty = 10


# def set_difficulty():
#   difficulty = input("Select Difficulty: easy or hard? ")
#   if difficulty == "hard"
#     return hard_difficulty
#   else
#     return easy_difficulty



def hard_mode(guess, lives, random_number):
        if guess < random_number:
          print("Too low")
          return lives-1

        elif guess > random_number:
          lives -=1
          print("too high")
          return lives
          
        else:
          print("Thats it!!!")

guess=0
while guess != random_number:
  guess= int(input("Guess a number: "))
  lives = hard_difficulty
  lives=hard_mode(guess,lives, random_number)
   
  if lives ==0:
    print("you ran out of guesses")
    
  elif guess!= random_number:
    print("guess again")
  