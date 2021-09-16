from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid = 0.7, stretch_len = 0.7)
        self.color("blue")
        self.refresh()

    def refresh(self):
        n_x = randint(-260, 260)
        n_y = randint(-260, 260)
        self.goto(n_x, n_y)
        self.speed(0)