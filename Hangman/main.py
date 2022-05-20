from module import play
from art import bar

if __name__ == "__main__":

    bar()
    play()

    while True:
        try_again = str(input("Type a letter to play again or type only enter to exit: "))

        if try_again != "":
            play()

        else:
            print("Game has ended.")
            break
            