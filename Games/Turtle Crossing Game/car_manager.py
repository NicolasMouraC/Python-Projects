import random
from random import choice, randint
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.list_of_cars = []
        self.speed = STARTING_MOVE_DISTANCE
    def createCars(self):
        if random.randint(1, 6) == 1:
            car = Turtle("square")
            car.penup()
            car.color(choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.goto(x=300, y=randint(-245, 245))
            self.list_of_cars.append(car)

    def carsMove(self):
        for i in self.list_of_cars:
            i.forward(self.speed)

    def levelPassed(self):
        self.speed += MOVE_INCREMENT
