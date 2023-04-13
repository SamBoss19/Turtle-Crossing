from turtle import Turtle
import random
colour = ['red', 'blue', 'green', 'yellow', 'violet', 'pink', 'purple']
locx  = [-350, -320, -290, -260, -230, -200, -170, -140, -110, -80, -50, -20, 10, 40, 70, 100, 130, 160, 190, 220, 250, 280, 310, 340]
locy = [-250, -230, -210, -190, -170, -150, -130, -110, -90, -70, -50, -30, -10, 10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Car():
    def __init__(self):
    
        self.allcars =[]
        self.carspeed = STARTING_MOVE_DISTANCE
       

        

    

    def othercars(self):
        prod = random.randint(1,6)
        if prod == 3:
            vehicle = Turtle()
            vehicle.shape("square")
            vehicle.shapesize(stretch_len=2, stretch_wid=0.5)
            vehicle.penup()
            vehicle.goto(-450, random.randint(-250, 250))
            vehicle.color(random.choice(colour))
            self.allcars.append(vehicle)

    def move(self):
        for cars in self.allcars:
            cars.forward(self.carspeed)
    def levelup(self):
        self.carspeed += MOVE_INCREMENT
            