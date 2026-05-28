word_list=["camel","rabbit","lion","tiger","giraffe","elephant"]
import random
lives=6

chosen_word=random.choice(word_list)
print(chosen_word)
placeholder=""
word_length=len(chosen_word)
for position in range(word_length):
    placeholder+="_"
print(placeholder)
game_over=False
correct_letters=[]
while not game_over:
    guess = input("guess a letter").lower()
    print(guess)
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display+=letter
        else:
            display += "_"
    print(display)
    if guess not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("you lose")
            print("***************YOU LOSE******************")
    if "_" not in display:
        game_over=True
        print("You win")
        print("***************YOU WIN******************")
    print(stages[lives])