from turtle import Turtle

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.scorex = 0
        self.scorey = 0
        self.up()
        self.goto(0, 250)
        self.color("white")
        self.write(f" {self.scorex} : {self.scorey}", move=False, align="center", font=("Arial", 28, "normal"))
        self.hideturtle()

    def increasel(self):
        self.scorex += 1
        self.clear()
        self.write(f" {self.scorex} : {self.scorey}", move=False, align="center", font=("Arial", 28, "normal"))
    def increaser(self):
        self.scorey += 1
        self.clear()
        self.write(f" {self.scorex} : {self.scorey}", move=False, align="center", font=("Arial", 28, "normal"))
