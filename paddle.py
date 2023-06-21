from turtle import Turtle

class Paddle (Turtle):
    def __init__(self,pos):
        super().__init__()
        self.new_paddle(pos)


    def new_paddle(self,pos):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(pos)



    def upp(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)

    def down(self):

        y = self.ycor()
        newy = y - 20
        self.goto(self.xcor(), newy)



