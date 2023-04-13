FONT = ("Cambria",15,"normal")
from turtle import Turtle 
class Score(Turtle):
        def __init__(self):
                super().__init__()
                self.level = 1
                self.penup()
                self.color("black")
                self.goto(-400,315)
                self.hideturtle()
                self.write(f"Level: {self.level}", move = False, align = "left", font = FONT)
        def gameover(self):
                self.goto(0,0)
                self.write(f"Gameover.", move = False, align = "center", font = ("Cambria",20,"normal"))

        def increase(self):
                self.clear()
                self.level +=1
                self.write(f"Level: {self.level}", move = False, align = "left", font = FONT)
