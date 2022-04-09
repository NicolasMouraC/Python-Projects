import time
from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard

__author__ = "Nicolas de Moura"
__version__ = 1.0
__date__ = "09/04/2022

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.tracer(0)
screen.title("Feito por um maranhese que quer vencer na vida")
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


screen.onkey(snake.move_north, key='w')
screen.onkey(snake.move_south, key="s")
screen.onkey(snake.move_east, key="d")
screen.onkey(snake.move_west, key="a")

game_main_flag = True
while game_main_flag:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.refresh_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.xcor() < -280:
        scoreboard.game_over()
        game_main_flag = False
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_main_flag = False

screen.exitonclick()
