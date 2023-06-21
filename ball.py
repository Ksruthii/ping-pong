from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.up()
        self.shapesize(0.5,0.5)
        self.goto(0,0)
        self.xmove=10
        self.ymove=10
        self.movespeed=0.1
    def move(self):
        newx=self.xcor()+self.xmove
        newy=self.ycor()+self.ymove
        self.goto(newx,newy)
        #self.bounce()
    def bounce_y(self):
        self.ymove *= -1
        self.movespeed*=0.9

    def bounce_x(self):
        self.xmove *= -1
        self.movespeed*=0.9
    def restart(self):
        self.goto(0,0)
        self.bounce_x()
        self.movespeed=0.1
