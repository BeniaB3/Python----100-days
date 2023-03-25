from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


def read_high_score():
    with open("data.txt") as data:
        high_score = data.read()
    return int(high_score)


def write_high_score(new_high_score):
    with open("data.txt", mode="w") as data:
        data.write(str(new_high_score))


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hight_score = read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.hight_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.hight_score:
            self.hight_score = self.score
            write_high_score(self.hight_score)
        self.score = 0
        self.update_scoreboard()
