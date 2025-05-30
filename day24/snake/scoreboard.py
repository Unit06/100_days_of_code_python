from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Aria", 18, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("highscore", mode="r") as file:
            self.high_score = int(file.read())
        self.score = 0
        # self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:  {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def eat_food(self):
        self.score += 1
        self.update_scoreboard()

