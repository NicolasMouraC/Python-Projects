from turtle import Turtle


class Player1Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=40, y=250)
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

    def refresh_score(self):
        """Add one point to player 1 score"""
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Arial", 24, "normal"))


class Player2Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=-40, y=250)
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

    def refresh_score(self):
        """Add one point to Player 2 score"""
        self.score += 1
        self.clear()
        self.write(self.score, align="center", font=("Arial", 24, "normal"))

