import turtle
import pandas


def count_your_score_read():
    with open("count.txt", "r") as file:
        content = file.read()
        count = int(content) if content else 0
    return count


def count_your_score_write(count):
    with open("count.txt", "w") as file:
        file.write(str(count))


def already_quess_read():
    with open("already_quess.txt", "r") as file:
        already_quess = file.read().split(",")
    return already_quess


def already_quess_write(state):
    with open("already_quess.txt", "a") as file:
        file.write(state + ",")

def update_picture(state_data):
   t = turtle.Turtle()
   t.hideturtle()
   t.penup()
   t.goto(int(state_data.x), int(state_data.y))
   t.write(state_data.state.item())


class us_game:
    def __init__(self):
        self.screen = turtle.Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape("blank_states_img.gif")
        self.image = "blank_states_img.gif"
        self.screen.addshape(self.image)
        turtle.shape(self.image)
        self.data = pandas.read_csv("50_states.csv")
        self.list_of_states = self.data.state.to_list()
        self.ready = already_quess_read()
        self.count = count_your_score_read()
        for state in self.ready:
            if state:
                state_data = self.data[self.data.state == state]
                update_picture(state_data)

    def run(self):
        while len(self.ready) <= 50:
            answer_state = self.screen.textinput(title=f"{self.count}/50 States Correct",
                                                 prompt="What's another state's name?")
            if answer_state.title() in self.list_of_states:
                if answer_state.title() not in self.ready:
                    self.ready.append(answer_state.title())
                    already_quess_write(answer_state.title())
                    self.count += 1
                    count_your_score_write(self.count)
                    t = turtle.Turtle()
                    t.hideturtle()
                    t.penup()
                    state_data = self.data[self.data.state == answer_state.title()]
                    t.goto(int(state_data.x), int(state_data.y))
                    t.write(answer_state.title())
                else:
                    print("You already guessed this state")
            elif answer_state == "Exit":
                break
            else:
                print("Wrong answer")


if __name__ == "__main__":
    game = us_game()
    game.run()
