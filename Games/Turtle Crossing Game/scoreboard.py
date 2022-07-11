from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-260, y=260)
        self.write(f"level : {self.level}", font=FONT)

    def levelUp(self):
        self.level += 1
        self.clear()
        self.write(f"level : {self.level}", font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over", font=FONT)
