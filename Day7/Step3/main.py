from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''

''']
for i in range(len(chosen_word)):
    display.append("_")
corrects = 0
lives = len(stages)-1
while lives > 0 and corrects < len(chosen_word):
    guess = input("Guess the letter: ").lower()
    k = 0
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            k += 1
            display[i] = guess
        
    if k > 0:
        print("Right!!")
    elif k == 0 and not guess in display:
        print("Wrong!!")
        lives -= 1
        print(stages[lives])
    else:
        print("You entered this letter before, please, enter a different letter!")
    corrects = 0
    for letter in display:
        if letter != "_":
            corrects += 1
    print(display)

if "_" not in display:
    print("You Win!!")
else:
    print("You lose")