from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    # Only move up
    def move(self):
        self.forward(20)
