from turtle import Turtle, Screen
import random

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# My solution, very simple
# for i in range(10):
#     angel = 360 / (i+3)
#     for j in range(i+3):
#         tim.forward(100)
#         tim.right(angel)

def change_color():
    R = random.random()
    B = random.random()
    G = random.random()
    tim.color(R, G, B)

def draw_shape(num_sides):
    angel = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angel)

for shape_side_n in range(3, 11):
    change_color()
    draw_shape(shape_side_n)

















screen = Screen()
screen.exitonclick()