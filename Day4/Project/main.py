from random import randint

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
game_images = [paper, scissors, rock]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if  user_choice < 0 or user_choice > 2:
    print("You entered an incorrect option, you lose!")
    quit()

print(game_images[user_choice])

computer_choice = randint(0,2)
print(f"Computer chose:\n{game_images[computer_choice]}")
if (computer_choice == 0 and user_choice == 2) or (computer_choice == 1 and user_choice == 0) or (computer_choice == 2 and user_choice == 1):
    print("You lose!!")
elif computer_choice == user_choice:
    print("Draw!!")
else:
    print("You win!!")


