from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

paddle_r = Paddle(350)
paddle_l = Paddle(-350)
scoreboard=Scoreboard()


screen.onkeypress(fun=paddle_r.up, key="Up")
screen.onkeypress(fun=paddle_r.down, key="Down")
screen.onkeypress(fun=paddle_l.up, key="w")
screen.onkeypress(fun=paddle_l.down, key="s")

ball = Ball()

game_is_on = True

while game_is_on:

    screen.listen()
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_wall()
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()


    if ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

    if ball.xcor() > 350:
        ball.reset_pos()
        scoreboard.l_point()

    if ball.xcor() < -350:
        ball.reset_pos()
        scoreboard.r_point()

screen.exitonclick()
