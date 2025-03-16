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


level = Scoreboard()
turtle = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(turtle.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
           game_is_on = False
           level.game_over()

    #Detect successful crossing
    if turtle.is_at_finish_line():
        turtle.go_to_start()
        car_manager.level_up()
        level.level_up()

screen.exitonclick()
