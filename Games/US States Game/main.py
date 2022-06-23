# Libraries to be used in the program
from turtle import Screen, Turtle
import pandas

# Variables to be used in the program
IMAGE = "blank_states_img.gif"
game_is_on = True
counter = 0
correct_states = []
missed_states = []

# Screen setup
screen = Screen()
turtle = Turtle()
screen.addshape(IMAGE)
turtle.shape(IMAGE)

# Data with the names and coordinates of the states
data = pandas.read_csv("50_states.csv")

# Creation of a turtle object to write the name of the state in the correct place
t = Turtle()
t.penup()
t.hideturtle()

# Game main loop
while game_is_on:
    # Get hold of the user answer
    answer = screen.textinput(title=f"States: {counter}/{len(data['state'])}", prompt="Type an estate:").title()

    # Checks if the user wants to exit the game by typing exit
    if answer == "Exit":
        break

    # Checks if the user has already typed all the states
    if counter == 50:
        game_is_on = False

    # Loop through the states data
    for row in data["state"]:
        # Checks if the user's answer is in a row
        if answer == row:
            counter += 1
            correct_states.append(answer)
            selected_row = data[data["state"] == row]
            # Get hold of the coordinates
            x_coordinate = int(selected_row.x)
            y_coordinate = int(selected_row.y)
            # Makes the turtle object write the state's name in the correct place
            t.goto(x=x_coordinate, y=y_coordinate)
            t.write(answer)
            break

# Loop through the states data
missed_states.append([state for state in data["state"] if state not in correct_states])
    # If it finds any state that haven't been typed, it put this state in a list
# Makes a file in CSV with the missed states
to_be_exported = pandas.DataFrame(missed_states)
to_be_exported.to_csv('to_be_exported')

