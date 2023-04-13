from turtle import Turtle, Screen
import random
from henry import Henry
from road import Car
from scoreboard import Score
import time
gameon = True
# 6207Impact
henry = Henry()
car = Car()
score = Score()

screen = Screen()
screen.setup(width = 900, height= 700)
screen.bgcolor("white")
screen.tracer(0)
screen.title("Turtle Crossing")
screen.listen()
screen.onkey(henry.up,"Up")

while gameon:
    time.sleep(0.1)
    screen.update()
    car.othercars()
    no = 1
    car.move()
    for cr in car.allcars:
        if cr.distance(henry) < 20:
            score.gameover()
            gameon = False
        
    if henry.ycor() > 350:
        car.levelup()
        score.increase()
        henry.goto(0,-300)







screen.exitonclick()