import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")


def random_colour():
    r = random.random()
    g = random.random()
    b = random.random()
    return r, g, b


for i in range(3, 10):
    angle = 360 / i
    for _ in range(i):
        tim.forward(100)
        tim.left(angle)
    tim.color(random_colour())

screen = t.Screen()
screen.exitonclick()
