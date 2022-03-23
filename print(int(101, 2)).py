import random

def get_word():
    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''
    return (random.choice(words.split()))
def play():
    word = get_word().upper
    tabs = " _ " * len(word)
    guessed_letter = []
    guessed = False
    tries = 6
    print("HANGMAN")
    while tries > 0:
        guess = str(input("Guess a letter: "))
        if len(guess) > 1:
            print("Please type only one letter per turn")
            while True:
                guess = str(input("Guess a letter: "))
                if len(guess) == 1:
                    break
        if guess in guessed_letter:
            print(f"{guess} already guessed")
            while True:
                guess = str(input("Guess a letter: "))
                if guess not in guessed_letter:
                    break
        if guess.upper() in word:
            print(f"Correct!\n there's a letter {guess} in the word")
        guessed_letter.append(guessed)
        tries -= 1

