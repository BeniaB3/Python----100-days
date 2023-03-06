import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(201, 164, 112), (239, 245, 241), (150, 75, 49), (222, 201, 136), (141, 30, 21), (221, 134, 147), (53, 93, 124), (176, 156, 46), (184, 88, 97), (44, 121, 86), (238, 165, 157), (26, 60, 55), (126, 31, 36), (160, 177, 210), (53, 42, 43), (215, 153, 162), (145, 182, 165), (27, 96, 71), (173, 191, 176), (232, 177, 171), (74, 44, 47), (135, 147, 31), (85, 127, 161), (172, 99, 108), (46, 64, 89), (16, 74, 84), (106, 127, 148)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()