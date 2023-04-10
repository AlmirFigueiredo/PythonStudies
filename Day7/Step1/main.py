from random import choice
word_list = ["aardvark", "baboon", "camel"]
word = choice(word_list)
user_guess = input("Guess a letter: ").lower()
for letter in word:
    if user_guess == letter:
        print("RIGHT")
    else:
        print("WRONG")