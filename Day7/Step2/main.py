from random import choice


word_list = ["aardvark", "baboon", "camel"]
chosen_word = choice(word_list)
display = []
for i in range(len(chosen_word)):
    display.append("_")
corrects = 0
wrongs = 0
while corrects < len(chosen_word) and wrongs < 4:
    guess = input("Guess the letter: ").lower()
    k = 0
    for i in range(len(chosen_word)):
        if guess == chosen_word[i]:
            k += 1
            display[i] = guess
        
    if k > 0:
        print("Right!!")
        corrects += 1
    else:
        print("Wrong!!")
        wrongs += 1
    print(display)
if "_" not in display:
    print("You Win!!")
else:
    print("You lose!")