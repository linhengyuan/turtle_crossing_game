import time
from turtle import Screen
from player import Player, Endline
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

# set control key
screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()

# end line
end_line = Endline()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Detect you win
    if player.distance(end_line) < 25:
        player.go_to_start()
        car_manager.level_up()
        scoreboard.level_up()


screen.exitonclick()  # keep the screen showing up