rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
  print("The number you gave is an invalid number.")
else:
  print(game_images[user_choice])

# Generates a random number between 0 and 2
computer_choice = random.randint(0, 2)
print(f"Computer chose {computer_choice}")
print(game_images[computer_choice])

# compare user_choice with computer_choice
if user_choice >= 3 or user_choice < 0:
  print("You typed in an invalid number. You lost.")
elif (user_choice == 0 and computer_choice == 1) or (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 0):
  print("Sorry, you lost.")
elif computer_choice == user_choice:
  print("It's a draw.")
else:
  print("Congrats, you won!")
