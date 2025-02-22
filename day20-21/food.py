from turtle import Turtle, Screen
import random

class Food(Turtle):

    def __init__(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)