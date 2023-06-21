from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
rpaddle = Paddle((380,0))
lpaddle = Paddle((-380,0))
screen = Screen()
screen.tracer(0)
screen.listen()
ball=Ball()
s=Score()


screen.setup(width=800, height=600)
screen.title("pong")
screen.bgcolor("black")
gameison=True
screen.onkey(rpaddle.upp, "Up")
screen.onkey(rpaddle.down, "Down")
screen.onkey(lpaddle.upp, "w")
screen.onkey(lpaddle.down, "s")
while gameison:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() >= 300 or ball.ycor() <=-300:
        ball.bounce_y()
    if ball.distance(rpaddle) < 50 and ball.xcor()>340 or ball.distance(lpaddle) < 50 and ball.xcor()<-340:
        ball.bounce_x()
    if ball.xcor()>400 :
        ball.restart()
        s.increasel()

    if ball.xcor()<-400 :
        ball.restart()
        s.increaser()






screen.exitonclick()
