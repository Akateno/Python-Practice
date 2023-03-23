import random

rock =0
paper=1
scissors=2

print("Lets Play Rock Paper Scissors")
choice=int(input("Choose Rorck, Paper or Scissors?"))

compChoice=random.randint(0,2)
print(f" I CHOOSE {compChoice}")

if compChoice==0 and choice==0:
    print("Its a tie")
elif compChoice==1:
    print("I WIN!!")
elif compChoice==2:
    print("You win :(")
else:
    print("Please choose a number between 0-2")



# if user_choice >= 3 or user_choice < 0: 
#   print("You typed an invalid number, you lose!") 
# elif user_choice == 0 and computer_choice == 2:
#   print("You win!")
# elif computer_choice == 0 and user_choice == 2:
#   print("You lose")
# elif computer_choice > user_choice:
#   print("You lose")
# elif user_choice > computer_choice:
#   print("You win!")
# elif computer_choice == user_choice:
#   print("It's a draw")