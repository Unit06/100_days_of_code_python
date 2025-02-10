from turtle import Turtle, Screen
import random

tim = Turtle()
tim.speed(10)
tim.pensize(15)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

for i in range(100):
    change_color()
    steps = random.randint(0, 10) * 10
    angle = random.randint(1, 4) * 90
    # tim.pensize(i)
    tim.right(angle)
    tim.forward(steps)

















screen = Screen()
screen.exitonclick()