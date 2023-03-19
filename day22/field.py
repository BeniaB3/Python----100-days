from turtle import Turtle


class Field(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 300)
        self.setheading(270)
        self.draw_field()


    def draw_field(self):
        for _ in range(15):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
