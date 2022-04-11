from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        """Make ball move"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounces the ball when it touches the wall """
        self.y_move *= -1

    def bounce_x(self):
        """Bounces the ball when it touches the paddle"""
        self.x_move *= -1

