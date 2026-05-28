import random

# Expanded word list
word_list = [
    "camel", "rabbit", "lion", "tiger", "giraffe", "elephant", "kangaroo", "hippopotamus",
    "rhinoceros", "zebra", "leopard", "cheetah", "chimpanzee", "gorilla", "buffalo",
    "panther", "koala", "flamingo", "peacock", "ostrich", "penguin", "crocodile", "alligator",
    "jaguar", "lynx", "antelope", "meerkat", "sloth", "armadillo", "porcupine"
]

# Hangman visual stages
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
display = ["_"] * word_length
lives = 6
guessed_letters = []
print("Welcome to Hangman!")
while True:
    print("\n" + " ".join(display))
    print(f"You have {lives} lives remaining.")
    print(stages[6 - lives])
    guess = input("Guess a letter: ").lower()
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.")
        continue
        if guess in guessed_letters:
            print(f"You've already guessed '{guess}'. Try another letter.")
            continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        lives -= 1
        print(f"'{guess}' is not in the word.")
        if lives == 0:
            print(stages[6])
            print(f"Game over! The word was '{chosen_word}'.")
            break

    if "_" not in display:
        print("\n" + " ".join(display))
        print("Congratulations! You guessed the word!")
        break
