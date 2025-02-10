from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(15)
tim.pensize(15)

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.pencolor(r, g, b)

for i in range(200):
    change_color()
    steps = random.randint(0, 10) * 10
    angle = random.randint(1, 4) * 90
    # tim.pensize(i)
    tim.right(angle)
    tim.forward(steps)

# small change















screen = Screen()
screen.exitonclick()