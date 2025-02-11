from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(20)
tim.pensize(1)

def change_color():
    r = random.random()
    b = random.random()
    g = random.random()
    tim.pencolor(r, g, b)

for _ in range(72):
    change_color()
    # angel += 1
    tim.circle(200)
    tim.right(5)


screen = Screen()
screen.exitonclick()
