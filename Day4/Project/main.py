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
choice_option = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")
if choice_option == "0":
    choice = rock
elif choice_option == "1":
    choice = paper
else:
    choice = scissors

