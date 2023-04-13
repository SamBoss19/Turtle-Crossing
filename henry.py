from turtle import Turtle
class Henry(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(0,-300)
        self.color('black')
        self.left(90)

    def up(self):
        self.forward(10)

    

