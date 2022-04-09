from random import randint
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
        self.refresh()
    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
