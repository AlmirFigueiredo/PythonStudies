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
choice_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
if  choice_option < 0 or choice_option > 2:
    print("You entered an incorrect option, you lose!")
    quit()

print(game_images[choice_option])

computer_choice = randint(0,2)
print(f"Computer chose:\n{game_images[computer_choice]}")




