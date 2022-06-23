from tkinter import *
import pandas
from random import choice

# Author information
__NAME__ = "Nicolas de Moura"
__GITHUB__ = "https://github.com/NicolasMouraC"
__DATE_ = "27/04/2022"

# -------------------- FUNCTIONS -------------------- #
# Changes the word in the card
def change_word():
    global current_word, timer
    current_word = choice(temp)
    window.after_cancel(timer)
    canvas.itemconfig(card, image=front_image)
    canvas.itemconfig(language, fill="black")
    canvas.itemconfig(language, text="English")
    canvas.itemconfig(word, fill="black")
    canvas.itemconfig(word, text=current_word["en"])
    # if the user waits 3 seconds, the card show the translation for the current word
    timer = window.after(3000, flip_card)


# A function that is triggered when the check button is pressed
def checked():
    global current_word
    global temp
    # Remove the word to make an unknown words dictionary
    temp.remove(current_word)
    change_word()


# A function that is triggered when the cross button is pressed
def dont_know():
    change_word()


# A function that is used to show the translation for the current word
def flip_card():
    global current_word
    canvas.itemconfig(card, image=back_image)
    canvas.itemconfig(language, fill="white")
    canvas.itemconfig(language, text="Portuguese")
    canvas.itemconfig(word, fill="white")
    canvas.itemconfig(word, text=current_word["pt-br"])


# -------------------- UI SETUP -------------------- #
# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_LANGUAGE = ("Arial", 40, "italic")
FONT_WORD = ("Arial", 60, "bold")
# Variable
current_word = {}

# Makes the main window
window = Tk()
window.title("Flash Cards")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR)

# A timer to check if the user wants the translation
timer = window.after(3000, flip_card)

# Try to check if the user has already opened the program and saved a file with unknown words
try:
    data = pandas.read_csv("data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/english_words.csv")

# Makes a temporary dictionary to leave the original data untouched
temp = data.to_dict(orient="records")

# Makes a canvas to make the program more user-friendly
canvas = Canvas(width=800, height=526, highlightthickness=0)

# Prepares the images and buttons to be used in the program
front_image = PhotoImage(file="images/card_front.png", )
back_image = PhotoImage(file="images/card_back.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, command=checked)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=dont_know)

# Setups the card
canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
card = canvas.create_image(400, 263, image=front_image,)
language = canvas.create_text(400, 150, font=FONT_LANGUAGE)
word = canvas.create_text(400, 260, font=FONT_WORD)

# Puts everything in place
canvas.grid(row=0, column=0, columnspan=2)
right_button.grid(row=1, column=0)
wrong_button.grid(row=1, column=1)

# Selects a random word to initialize the program
change_word()

# Keeps running until the user closes the program
window.mainloop()

# At the end of the program, it writes the remaining and unknown words on a file
with open("data/to_learn.csv", mode="w", encoding="utf-8") as to_learn:
    temporary = pandas.DataFrame(temp)
    temporary.to_csv(to_learn, index=False)
