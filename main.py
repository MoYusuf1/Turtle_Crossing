import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from road import Road
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.tracer(0)
score = Scoreboard()
road = Road()
# tells the program to expect input
screen.listen()

# the player is spawned in
player = Player()

# these multiple cars are spawned in
jeep = CarManager()
acura = CarManager()
honda = CarManager()
ford = CarManager()
toyota = CarManager()
mercedes = CarManager()
benz = CarManager()
jeep1 = CarManager()
acura1 = CarManager()
honda1 = CarManager()
ford1 = CarManager()
toyota1 = CarManager()
mercedes1 = CarManager()
benz1 = CarManager()
jeep2 = CarManager()
acura2 = CarManager()
honda2 = CarManager()
ford2 = CarManager()
toyota2 = CarManager()
mercedes2 = CarManager()
benz2 = CarManager()


# key binds
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

# finish line turtles

cpu1_turtle = Player()
cpu1_turtle.color("black")
cpu2_turtle = Player()
cpu2_turtle.color("orange")
cpu3_turtle = Player()
cpu3_turtle.color("blue")

cpu1_turtle.goto(-40, 220)
cpu2_turtle.goto(10, 250)
cpu3_turtle.goto(50, 200)




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cpu1_turtle.forward(0.1)
    cpu2_turtle.forward(0.1)
    cpu3_turtle.forward(0.1)

    # the cars will now drive
    jeep.reset_position()
    acura.reset_position()
    honda.reset_position()
    ford.reset_position()
    toyota.reset_position()
    mercedes.reset_position()
    benz.reset_position()
    jeep1.reset_position()
    acura1.reset_position()
    honda1.reset_position()
    ford1.reset_position()
    toyota1.reset_position()
    mercedes1.reset_position()
    benz1.reset_position()
    jeep2.reset_position()
    acura2.reset_position()
    honda2.reset_position()
    ford2.reset_position()
    toyota2.reset_position()
    mercedes2.reset_position()
    benz2.reset_position()

    # detects collision
    if jeep.distance(player) < 20 or acura.distance(player) < 20 or honda.distance(player) < 20 \
            or ford.distance(player) < 20 or toyota.distance(player) < 20 or mercedes.distance(player) < 20 \
            or benz.distance(player) < 20 or jeep1.distance(player) < 20 or acura1.distance(player) < 20 or honda1.distance(player) < 20 \
            or ford1.distance(player) < 20 or toyota1.distance(player) < 20 or mercedes1.distance(player) < 20 \
            or benz1.distance(player) < 20 or jeep2.distance(player) < 20 or acura2.distance(player) < 20 or honda2.distance(player) < 20 \
            or ford2.distance(player) < 20 or toyota2.distance(player) < 20 or mercedes2.distance(player) < 20 \
            or benz2.distance(player) < 20:
        game_is_on = False

    if player.ycor() > 300:
        score.increase_score()
        player.goto(0, -250)


