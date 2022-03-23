from random import randint
state = ['''
+---+       
|       
|
|
===''', 
'''
+---+
O   |
|
|
===''', 
'''
+---+
O   |
|   |
|
===''', 
'''
+---+
O   |
/|   |
|
===''', 
'''
+---+
O   |
/|\  |
|
===''', 
'''
+---+
O   |
/|\  |
/    |
===''', 
'''
+---+
O   |
/|\  |
/ \  |
===''']
words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
lion lizard llama mole monkey moose mouse mule newt otter owl panda
parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
skunk sloth snake spider stork swan tiger toad trout turkey turtle
weasel whale wolf wombat zebra'''.split()
class Hangman():
    def random_word(wordlist):
        word = wordlist[randint(0, (len(wordlist) - 1))]
        Hangman.starter_board(word)
    def starter_board(word):
        bars = " _ " * len(word)
        print(bars)
        print("\nThe word has {} letters".format(len(word)))
        yield bars
    def check_board(letter, word):
        if letter in word:
            print("{} is in the word".format(letter))
    
        else:
            print("{} is not in the word".format(letter))
    def guessed_letter(word):
        guessed = str(input("Type a letter:\n"))
        if guessed[0:1] in word:
            print("{} is in the word".format(guessed[0:1]))
        

if __name__ == "__main__":
    Hangman.random_word(words)