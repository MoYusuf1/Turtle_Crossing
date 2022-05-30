from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(random.randrange(-200, 200), random.randrange(-200, 200))

    def reset_position(self):
        self.forward(random.randrange(10, 30))
        if self.xcor() < -300:
            x_position = self.xcor() + 600
            y_position = random.randrange(-200, 200)
            self.goto(x=x_position, y=y_position)
