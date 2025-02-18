from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)

def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

game_is_on = True


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    # snake.move()

    #Detect collision with food
    # if snake.head.distance(food) < 15:
    #    food.refresh()
    #    snake.extend()
    #    score.eat_food()

    #Detect collision with wall
    #if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #    game_is_on = False
    #    score.game_over()

    #Detect collision with tail
    #for segment in snake.snake[1:]:
    #    if snake.head.distance(segment) < 10:
    #        game_is_on = False
    #        score.game_over()

screen.exitonclick()