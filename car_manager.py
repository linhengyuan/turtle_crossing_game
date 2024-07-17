from turtle import Turtle, Screen
from random import randint,choice
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

screen = Screen()

class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        rand_chance = randint(1,6)
        if rand_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

