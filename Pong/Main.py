#Libraries used
import time
from turtle import Screen
from Paddle import Paddle1, Paddle2
from Scoreboard import Player1Score, Player2Score
from Ball import Ball

#Informations
__author__ = "Nicolas de Moura"
__version__ = 1.0
__date__ = "11/04/2022"

#Screen setup
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("Black")
screen.title("Pong Game")
screen.tracer(0)
screen.listen()

#players setup
player1_score = Player1Score()
player2_score = Player2Score()
player1_paddle = Paddle1()
player2_paddle = Paddle2()

#Ball setup
ball = Ball()

#Button to be used in the game
screen.onkey(player1_paddle.move_up, "w")
screen.onkey(player1_paddle.move_down, "s")
screen.onkey(player2_paddle.move_up, "8")
screen.onkey(player2_paddle.move_down, "2")

#Game start
if __name__ == "__main__":
    game_flag = True
    while game_flag:
        time.sleep(0.1)
        screen.update()
        ball.move()

        #if the ball touches the the wall, it bounces
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        #if the player 2 cant reach the ball, point to player 1
        if ball.xcor() > 380:
            player1_score.refresh_score()
            ball.goto(0, 0)
        #if the player 1 cant reach the ball, point to player 2
        if ball.xcor() < -380:
            player2_score.refresh_score()
            ball.goto(0, 0)
        #make the ball bounce when it touches the paddle
        if ball.distance(player1_paddle) < 50 and ball.xcor() < -320 or ball.distance(player2_paddle) < 50 and ball.xcor() > 320:
            ball.bounce_x()

screen.exitonclick()
