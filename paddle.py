from turtle import Turtle

p1 = Turtle()
c= p1.ycor()
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.shape("square")
        self.shapesize(5, 1, 0)
        self.color("white")
        self.penup()

    def up(self):
        global c
        if c>=250:
            c=c
        else:
            c=c+50
        self.sety(c)

    def down(self):
        global c
        if c<=-250:
            c=c
        else:
            c = c - 50
        self.sety(c)

    def p2_movement(self):
        self.goto(360, 280)
        self.goto(360, -280)