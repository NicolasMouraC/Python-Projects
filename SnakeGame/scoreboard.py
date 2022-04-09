from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=260)
        self.write(f"{self.score}", align="center", font=("Arial", 24, "normal"))
    def refresh_score(self):
        self.score += 1
        self.clear()
        self.write(f"{self.score}", align="center", font=("Ariel", 24, "normal"))
    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=("Arial", 24, "normal"))
