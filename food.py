from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super(Food, self).__init__()
        self.pencolor("purple")
        self.penup()
        self.shape("circle")
        self.speed("fastest")
        self.shapesize(0.5, 0.5)
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))