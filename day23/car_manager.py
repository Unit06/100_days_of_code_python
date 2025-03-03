from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choices(COLORS))
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.left(90)
        self.x_position = random.randint(300, 400)
        self.y_position = random.randint(-260, 260)
        self.penup()
        self.goto(self.x_position, self.y_position)

    def move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())