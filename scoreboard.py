from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.game_level = 0
        self.goto(x= -270, y = 250)
        self.write(f"Level: {self.game_level}", align="left" , font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_up(self):
        self.game_level += 1
        self.clear()
        self.write(f"Level: {self.game_level}", align="left" , font=FONT)
