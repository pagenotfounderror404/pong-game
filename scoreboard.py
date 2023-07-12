from turtle import Turtle
t=Turtle()
score1=Turtle()
score2=Turtle()
class Scoreboard:

    def make_boundary(self):
        t.ht()
        t.pencolor("white")
        t.width(5)
        b = True
        c = 300
        t.penup()
        t.goto(0, 300)
        while b:
            t.pendown()
            t.goto(0, c)
            c = c - 10
            t.goto(0, c - 10)
            c = c - 30
            t.penup()
            t.goto(0, c)
            if c <= -300:
                b = False

    def right_Score(self,s):
        score1.ht()
        score1.clear()
        score1.penup()
        score1.goto(50, 230)
        score1.pencolor("white")
        score1.write(s, align="center", font=('Arial', 50, 'bold'))

    def left_Score(self,s):
        score2.ht()
        score2.clear()
        score2.penup()
        score2.goto(-50, 230)
        score2.pencolor("white")
        score2.write(s, align="center", font=('Arial', 50, 'bold'))
