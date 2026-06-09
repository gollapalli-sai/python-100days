from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
DATA_FILE = os.path.join(os.path.dirname(__file__), "data.txt")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open(DATA_FILE) as data:
                self.high_score = int(data.read())
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
