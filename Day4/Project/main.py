from random import randit

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
choice_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(game_images[choice_option])

computer_choice = randit(0,2)



