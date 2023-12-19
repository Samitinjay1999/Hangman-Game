import random as r
import os
from Projects.hangmanFiles import HangmanStagesList as sList
from Projects.hangmanFiles import FruitsListForHangman as fList
random_fruit = r.choice(fList.fruits)
random_fruit = str.casefold(random_fruit)
print(random_fruit)
word_list = []
for i in range(len(random_fruit)):
    word_list.append("_")

print(word_list)
lives = len(sList.hangman_stages)-1
flag = 1
while lives != 0:
    print("----------- HANGMAN GAME ------------")
    Guessed_letter = input("Guess a letter: ").lower()
    for i in range(len(random_fruit)):
        if random_fruit[i] == Guessed_letter:
            word_list[i] = Guessed_letter
    if Guessed_letter not in random_fruit:
        lives -= 1
        print(f"Wrong, You lost a life, lives: {lives}")
    else:
        print("Nice")
        print(f"Remaining lives: {lives}")
    print(sList.hangman_stages[lives])
    print(f"lives : {lives}")
    print(word_list)
    for i in word_list:
        if i == '_':
            break
    else:
        flag = 0
    if flag == 0:
        print("Congratulations, You win...")
        break
    os.system('cls')
if lives == 0:
    print("you loose...")

