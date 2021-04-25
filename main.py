from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from whiteline import Whiteline
from dashedline import Dashedline
import time

screen = Screen()
screen.setup(width=1000, height=700)
screen.bgcolor("black")
screen.title("Jackson's Pong Game")
screen.tracer(0)

r_paddle = Paddle((480,0))
l_paddle = Paddle((-480,0))

scoreboard = Scoreboard()
whiteline = Whiteline()

dashedline = Dashedline()
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 240 or ball.ycor() < -320:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 460:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -460:
        ball.bounce_x()

     # Detect R paddle misses:
    if ball.xcor() > 480:
        ball.reset_position()
        scoreboard.l_point()
     # Detect L paddle misses:
    elif ball.xcor() < -480:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()