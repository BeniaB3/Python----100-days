from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from field import Field
import time

my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("Pong Game")
my_screen.tracer(0)

my_paddleRight = Paddle((350, 0))
my_paddleLeft = Paddle((-350, 0))

my_ball = Ball()
scoreboard = Scoreboard()
field = Field()


my_screen.listen()
my_screen.onkey(my_paddleRight.go_up, "Up")
my_screen.onkey(my_paddleRight.go_down, "Down")
my_screen.onkey(my_paddleLeft.go_up, "w")
my_screen.onkey(my_paddleLeft.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(my_ball.move_speed)
    my_screen.update()
    my_ball.move()

    # Detect collision with wall
    if my_ball.ycor() > 280 or my_ball.ycor() < -280:
        my_ball.bounce_y()

    # Detect collision with left paddle
    if my_ball.distance(my_paddleRight) < 50 and my_ball.xcor() > 320 or my_ball.distance(
            my_paddleLeft) < 50 and my_ball.xcor() < -320:
        my_ball.bounce_x()

    # Detect when right paddle misses
    if my_ball.xcor() > 380:
        my_ball.reset_position()
        scoreboard.l_point()
        my_ball.reset_move_speed()

    if my_ball.xcor() < -380:
        my_ball.reset_position()
        scoreboard.r_point()
        my_ball.reset_move_speed()

    if scoreboard.game_over():
        game_is_on = False

my_screen.exitonclick()
