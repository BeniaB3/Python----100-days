from random import randint
import turtle

tim = turtle.Turtle()

# shape of tim
tim.shape("turtle")
# make tim trace bigger
tim.pensize(10)
direction = 0
# faster
tim.speed(10)

# create a Screen object and set the color mode
screen = turtle.Screen()
screen.colormode(255)


def random_colour():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_Color = (r, g, b)
    return random_Color


def random_direction():
    global direction
    old_dir = direction
    direction = randint(0, 4)
    if old_dir != direction:
        tim.color(random_colour())


def move():
    global direction
    while True:
        tim.forward(20)
        random_direction()
        if direction == 0:
            tim.right(90)
        elif direction == 1:
            tim.left(90)
        elif direction == 2:
            tim.right(180)
        elif direction == 3:
            tim.left(180)


move()
screen.exitonclick()
