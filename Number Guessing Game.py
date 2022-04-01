import random

__author__ = "Nicolas de Moura"
__date__ = "01/04/2022"
__version__ = 1.2

class NumberGuessing:
    def __init__(self):
        self.art = '''
 _  _  __  __  __  __  ____  ____  ____     ___  __  __  ____  ___  ___  ____  _  _  ___     ___    __    __  __  ____ 
( \( )(  )(  )(  \/  )(  _ \( ___)(  _ \   / __)(  )(  )( ___)/ __)/ __)(_  _)( \( )/ __)   / __)  /__\  (  \/  )( ___)
 )  (  )(__)(  )    (  ) _ < )__)  )   /  ( (_-. )(__)(  )__) \__ \\__ \ _)(_  )  (( (_-.  ( (_-. /(__)\  )    (  )__) 
(_)\_)(______)(_/\/\_)(____/(____)(_)\_)   \___/(______)(____)(___/(___/(____)(_)\_)\___/   \___/(__)(__)(_/\/\_)(____)
'''
        self.number = random.randint(1, 100)
    def game(self):
        print(self.art)
        while True:
            while True:
                self.difficult = input("-Choose a dificulty level-\nType 'easy' or 'hard: ").lower()
                if self.difficult == 'easy':
                    print("Easy difficulty setted")
                    self.tries = 10
                    break
                elif self.difficult == 'hard':
                    print("Hard difficulty setted")
                    self.tries = 5
                    break
                else:
                    print(f"{self.difficult} is not recognized as a difficulty")
            while True:
                if self.tries == 0:
                    print("You ran out of tries")
                    print(f"The correct number was {self.number}")
                    break
                print(f"You have {self.tries} left")
                self.guess = int(input("Type a number: "))
                if self.guess == self.number:
                    print(f"You did it!\n{self.guess} was the correct number.")
                    break
                elif self.guess > self.number:
                    if (self.guess - self.number) > 20:
                        print(f"The number is much lower than {self.guess}")
                        self.tries -= 1
                    else:
                        print(f"The number is lower than {self.guess}")
                        self.tries -= 1
                elif self.guess < self.number:
                    if (self.guess - self.number) < -20:
                        print(f"The number is much higher than {self.guess}")
                        self.tries -= 1
                    else:
                        print(f"The number is higher than {self.guess}")
                        self.tries -= 1
            if input("Continue?\nTab enter key to continue or any other key to exit: ") == '':
                continue
            else:
                print("Exiting...")
                break
if __name__ == "__main__":
    game = NumberGuessing()
    game.game()