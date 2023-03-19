from turtle import Turtle

FONT = ("Courier", 24, "normal")

LVL = 1


class Scoreboard:

    def __init__(self):
        super().__init__()
        self.level = LVL
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.penup()
        self.scoreboard.goto(-280, 250)

    def update_scoreboard(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Level: {self.level}", align="left", font=FONT)

    def game_over(self):
        self.scoreboard.goto(-60, 0)
        self.scoreboard.write(f"GAME OVER", align="center", font=FONT)


