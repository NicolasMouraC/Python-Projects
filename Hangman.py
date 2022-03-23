from gettext import find
import random
word = ""
def get_word():
    words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''
    return (random.choice(words.split()))
def find_index(letterGuessed,wordToBeGuessed, tabs):
    indexes = []
    index = wordToBeGuessed.find(letterGuessed)
    indexes.append(str(index))
    if index != wordToBeGuessed.rfind:
        index2 = wordToBeGuessed.rfind(letterGuessed)
        indexes.append(str(index2))
    for item in indexes:
        item = indexes[int(item) - 1]
        tabs = tabs[int(item)] + letterGuessed + tabs[int(item) + 1:]
    return tabs
def play():
    global word 
    word = get_word().upper()
    print(word)
    tabs = "_" * len(word)
    guessed_letter = []
    guessed = False
    tries = 6
    print("HANGMAN")
    print(tabs)
    while tries > 0:
        guess = str(input("Guess a letter: ").upper())
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
        if word.find(guess):
            print(f"Correct!\nThere's letter {guess} in the word")
            #letter_guessed = find_index(guess, word)
            find_index(guess, word, tabs)
            print(tabs)
        else:
            print(f"Wrong! there's no letter {guess} in the word")
            #Hangman print
        if():
            pass
        #Check the won condition    
        guessed_letter.append(guessed)
        tries -= 1
if __name__ == "__main__":
    play()
