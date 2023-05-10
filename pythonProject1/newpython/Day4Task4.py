import random

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

game_images = [rock, paper, scissors]

user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n")
user_choice_int = int(user_choice)
print(game_images[user_choice_int])
computer_choice = random.randint(0,2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice_int == 0 and computer_choice == 2:
    print("You won")
if user_choice_int == 2 and computer_choice == 0:
    print("Computer won")
elif computer_choice > user_choice_int:
    print("Computer won")
elif computer_choice == user_choice_int:
    print("It's a draw")
else:
    print("You won")
