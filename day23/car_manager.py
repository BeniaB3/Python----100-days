from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

MORE_CARS = 6


def random_color():
    return random.choice(COLORS)


def if_make_new_car():
    return random.randint(1, MORE_CARS) == 1


class CarManager:

    def __init__(self):
        super().__init__()
        self.car = None
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if if_make_new_car():

            self.car = Turtle()
            self.car.shape("square")
            self.car.shapesize(stretch_wid=1, stretch_len=2)
            self.car.color(random_color())
            self.car.penup()
            self.car.goto(300, random.randint(-250, 250))
            self.car_list.append(self.car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def destroy_car(self):
        for car in self.car_list:
            if car.xcor() < -310:
                car.hideturtle()
                self.car_list.remove(car)
                del car

    def level_up(self):
        global MORE_CARS
        if MORE_CARS > 1:
            MORE_CARS -= 1
        self.car_speed += MOVE_INCREMENT

