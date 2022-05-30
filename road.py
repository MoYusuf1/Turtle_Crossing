from turtle import Turtle
import random


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("grey")
        self.setheading(180)
        self.goto(0, 0)
        self.shapesize(stretch_wid=20, stretch_len=30)
