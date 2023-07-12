import random
from turtle import Turtle
x=0
y=0
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.newy=15
        self.newx=15
        self.speedmove=0.1
    def bouncey(self):
            self.newy*=-1
    def bouncex(self):
            self.newx*=-1
            self.speedmove*=0.7
    def move(self):
        global x,y
        x= self.xcor()+self.newx
        y= self.ycor()+self.newy
        self.goto(x,y)
        if self.ycor() > 280 or self.ycor() < -280:
            self.bouncey()
    def reset(self):
        self.goto(0,0)
        self.speedmove=0.1
        self.bouncex()





