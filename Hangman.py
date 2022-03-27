import sys
from random import choice
class Hangman:
    def __init__(self):
        self.error_out_tries = "Ran out of Tries"
        self.words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''
        self.word = choice(self.words.split())
        self.tabs = "_" * len(self.word)
        self.tries = 6
        self.correct_letters = ""#[char for char in self.word]
    def play(self):
        print("HANGMAN")
        print(self.word)
        print(self.tabs)
        while True:
            print(f"You Have: {self.tries} left")
            self.letter = str(input("Type a letter: "))
            if self.letter[0] in self.word:
                print(f"{self.letter[0]} in word")
                self.c_letter = self.letter[0]
                for i in range(len(self.word)):
                    if self.word[i] in self.c_letter:
                        self.tabs = self.tabs[:i] + self.c_letter + self.tabs[i+1:]
                print(self.tabs)
                self.correct_letters += self.c_letter
                if self.correct_letters == self.word:
                    print("You Won!")
                    sys.exit()
            elif self.letter[0] not in self.word:
                print(f"{self.letter[0]} not in word")
                self.tries -= 1
                if self.tries < 1:
                    print("You ran out of tries")
                    raise Exception(self.error_out_tries)

if __name__ == "__main__":
    Play = Hangman()
    Play.play()
