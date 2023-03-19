from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        super().__init__()
        self.turtle = None
        self.create_turtle()
        self.go_to_start()

    def create_turtle(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.penup()
        self.turtle.setheading(90)

    def go_to_start(self):
        self.turtle.goto(STARTING_POSITION)

    def go_up(self):
        self.turtle.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        return self.turtle.ycor() > FINISH_LINE_Y






