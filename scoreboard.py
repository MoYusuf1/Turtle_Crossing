from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-150, 240)
        self.write(f"SCORE: {self.score}", align="center", font=("Arial", 25, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
