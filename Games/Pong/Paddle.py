from turtle import Turtle

class Paddle1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x=-350, y=0)

    def move_up(self):
        """Make the paddle move up"""
        self.goto(self.xcor(), self.ycor() + 20)

    def move_down(self):
        """Make the paddle move down"""
        self.goto(self.xcor(), self.ycor()- 20)

class Paddle2(Paddle1):
    def __init__(self):
        super().__init__()
        self.goto(x=350, y=0)

