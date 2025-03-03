import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle ROAD")
screen.tracer(0)
cars = []

level = Scoreboard()
turtle = Player()

for car_index in range(0,10):
    new_car = CarManager()
    cars.append(new_car)

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()

    if turtle.ycor() >= 280:
        level.level_up()
        turtle.reset_position()

screen.exitonclick()
