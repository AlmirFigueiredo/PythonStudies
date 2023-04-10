from random import choice

word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = []
for i in range(len(chosen_word)):
    display.append("_")
    
guess = input("Guess the letter: ").lower()
for pos in range(len(display)):
    if chosen_word[pos] == guess:
        print("Right")
        display[pos] = guess
    
print(display)