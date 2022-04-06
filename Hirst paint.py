__author__ = "Nicolas de Moura"
__date__ = "06/04/2022"

from random import randint
from turtle import Turtle, Screen
colors = [(235, 234, 231), (234, 229, 231), (236, 35, 108), (221, 232, 237), (145, 28, 64), (239, 75, 35),
 (6, 148, 93), (232, 238, 234), (231, 168, 40), (184, 158, 46), (44, 191, 233), (27, 127, 195), (126, 193, 74),
 (253, 223, 0), (85, 28, 93)]
x = -250
y = -225

def random_color(color):
    r = color[randint(0, (len(color) - 1))][0]
    g = color[randint(0, (len(color) - 1))][1]
    b = color[randint(0, (len(color) - 1))][2]
    rgb = (r, g, b)
    return rgb

turtle = Turtle()
screen = Screen()
screen.colormode(255)
turtle.hideturtle()
turtle.penup()
turtle.setposition(x, y)

for i in range(100):
    turtle.dot(20, random_color(colors))
    turtle.forward(50)
    if turtle.xcor() == 250:
        y += 50
        turtle.setposition(x, y)

screen.exitonclick()