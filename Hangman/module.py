from random import choice
from time import sleep
from art import logo, stickman


def play():

    words = '''ant baboon badger bat bear beaver camel cat clam snake puma
    coyote crow deer dog donkey duck eagle hurricane fox frog goat goose falcon
    lion lizard llama mole monkey moose merman mouse otter owl panda
    parrot pigeon python rabbit ram mouse crow rhino salmon seal shark sheep
    prawn sloth snake spider stork swan tiger frog trout turkey turtle
    weasel whale wolf wombat zebra'''
    word = choice(words.split())
    tabs = "_" * len(word)
    correct_letter = ''
    guessed_letter = []
    index = 0

    print(logo)
    sleep(0.15)
    print(tabs)
    sleep(0.15)
    print(f"The word has {len(word)} letters.")
    print("You have 6 tries.")

    while True:
        sleep(0.25)
        letter = str(input("Type letters: ")).lower()
        sleep(0.25)

        try:
            if int(letter):
                print("This game only allow letters.")
                sleep(0.25)

        except ValueError:
            if letter == '':
                print("Please, type a letter.")
                sleep(0.25)

            elif letter in guessed_letter:
                print(f"Letter {letter.upper()} was already entered.")
                sleep(0.25)

            else:
                if letter[0] in word:
                    print(f"{letter[0].upper()} is in the word!")
                    correct_letter += letter[0]
                    for i in range(len(word)):
                        if word[i] in correct_letter:
                            tabs = tabs[:i] + word[i] + tabs[i + 1:]
                    guessed_letter.append(letter[0])

                    print(tabs)
                    sleep(0.25)
                    if "_" not in tabs:
                        print("You won!")
                        break

                elif letter[0] not in word:
                    print(f"{letter[0].upper()} is not in the word.")
                    sleep(0.25)
                    print(stickman[index])
                    sleep(0.25)
                    print(tabs)
                    index += 1
                    guessed_letter.append(letter[0])

                    if index == 7:
                        print("You ran out of tries.")
                        break
