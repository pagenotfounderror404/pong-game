import time
from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

s=Screen()
p1=Paddle()
p2=Paddle()
score=Scoreboard()
b=Ball()

s.setup(height=600,width=800)
s.bgcolor("black")
s.title("Pong")

p1.goto(-360, 0)
p1.showturtle()
p2.goto(360, 0)
p2.showturtle()
score.make_boundary()
score.left_Score(0)
score.right_Score(0)

r=0
l=0

w=int(s.textinput(title="Score", prompt="Set the winning score"))
s.listen()
s.onkey(p1.up,"Up")
s.onkey(p1.down,"Down")
s.onkey(p2.up, "Right")
s.onkey(p2.down, "Left")







game_is_on=True


while game_is_on:
    time.sleep(0.1)
    s.update()
    b.move()
    if b.distance(p2) < 50 and b.xcor() > 350 or b.distance(p1) < 50 and b.xcor() < -350:
        b.bouncex()
    if  b.distance(p2) > 50 and b.xcor() > 400:
        b.reset()
        l+=1
        score.left_Score(l)
    if  b.distance(p1) > 50 and b.xcor() < -400:
        b.reset()
        r+=1
        score.right_Score(r)
    if l==w:
        game_is_on=False
        print("The winner is the left paddle")
        exit()
    if r==w:
        game_is_on=False
        print("The winner is the right paddle")
        exit()














s.exitonclick()