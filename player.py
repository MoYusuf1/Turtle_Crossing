from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.goto(x=0, y=-250)

    def move_up(self):
        x_position = self.xcor()
        y_position = self.ycor() + MOVE_DISTANCE
        self.goto(x_position, y_position)

    def move_down(self):
        x_position = self.xcor()
        y_position = self.ycor() - MOVE_DISTANCE
        self.goto(x_position, y_position)


