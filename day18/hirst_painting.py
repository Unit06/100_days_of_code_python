# import colorgram
import turtle
from turtle import Turtle, Screen
import random

# Extract colors from picture
# colors_extract = colorgram.extract('paint.jpg', 50)
# for color in colors_extract:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tuple = (r,g,b)
#     colors_list_rgb.append(new_tuple)

colors_list_rgb = [(144, 76, 50), (188, 165, 117), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81),
                   (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93),
                   (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82),
                   (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201),
                   (213, 182, 176), (37, 47, 45), (14, 101, 109), (188, 190, 201), (11, 112, 104), (65, 66, 58)]

turtle.colormode(255)
tim = Turtle()

# ----prepare Tim----
tim.shape("circle")
tim.penup()
tim.speed(10)
tim.right(180)
tim.forward(250)
tim.right(180)
# -------------------

for i in range(10):
    color = random.choice(colors_list_rgb)
    tim.dot(20,color)
    tim.forward(50)

screen = Screen()
screen.exitonclick()
