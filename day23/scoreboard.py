from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.game_level = 0
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-205, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level : {self.game_level}", align=ALIGNMENT, font=FONT)

    def level_up(self):
        self.game_level += 1
        self.clear()
        self.update_scoreboard()