
# libraries used in game
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# file information
__author__ = "Nicolas de Moura"
__version__ = 1.0
__date__ = "13/04/22"

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# GUI setup
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Controls setup
screen.onkey(player.move, "Up")

# Game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.createCars()
    car_manager.carsMove()

    # Checks if the turtle has reached the on the top
    if player.ycor() > 280:
        player.goto(x=0, y=-280)
        scoreboard.levelUp()
        car_manager.levelPassed()

    # Checks if the turtle collided with a car
    for car in car_manager.list_of_cars:
        if car.distance(player) < 20:
            scoreboard.gameOver()
            game_is_on = False

# Wait for a mouse click when the game is over to close the window
screen.exitonclick()
