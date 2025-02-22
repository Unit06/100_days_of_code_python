from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Aria", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r = 0
        self.score_l = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_l}  :  {self.score_r}", align=ALIGNMENT, font=FONT)

    def l_goal(self):
        self.score_l += 1
        self.clear()
        self.update_scoreboard()

    def r_goal(self):
        self.score_r += 1
        self.clear()
        self.update_scoreboard()
