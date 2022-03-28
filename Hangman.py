from time import sleep
import sys
from random import choice
class Hangman:
    def __init__(self):
        self.words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''
        self.word = choice(self.words.split())
        self.tabs = "_" * len(self.word)
        self.c_letter = ''
        self.gueesed_letters = ''
        self.hangman_index = 0
        self.hangman = ['''
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
    def play(self):
        print("HANGMAN")
        sleep(0.15)
        print(self.tabs)
        sleep(0.15)
        print(f"The word has {len(self.word)} letter")
        print("You have 6 tries")
        sleep(0.1)
        while True:
            sleep(0.25)
            self.letter = str(input("Type a letter: ")).lower()
            sleep(0.25)
            try:
                if int(self.letter):
                    print("This program does not allow numbers")
                    sleep(0.25)
            except:
                if self.letter == '':
                    print("Please enter a letter")
                    sleep(0.25)
                elif self.letter in self.gueesed_letters:
                    print(f"{self.letter} was already guessed")
                    sleep(0.25)
                else:
                    if self.letter[0] in self.word:
                        print(f"{self.letter[0]} in word")
                        self.c_letter += self.letter[0]
                        for i in range(len(self.word)):
                            if self.word[i] in self.c_letter:
                                self.tabs = self.tabs[:i] + self.word[i] + self.tabs[i+1:]
                        self.gueesed_letters += self.letter[0]
                        print(self.tabs)
                        sleep(0.25)
                        if "_" not in self.tabs:
                            print("You Won!")
                            break
                    elif self.letter[0] not in self.word:
                        print(f"{self.letter[0]} not in word")
                        sleep(0.25)
                        print(self.hangman[self.hangman_index])
                        sleep(0.25)
                        print(self.tabs)
                        self.hangman_index += 1
                        self.gueesed_letters += self.letter[0]
                        if self.hangman_index == 7:   
                            print("Ran out of Tries")
                            break

if __name__ == "__main__":
    Play = Hangman()
    Play.play()
    while True:
        try_again = str(input("Type ENTER to play again or any other key to exit: "))
        if try_again == "":
            Play.play()
        else:
            print("Exiting...")
            sleep(0.15)
            sys.exit("Program terminated")