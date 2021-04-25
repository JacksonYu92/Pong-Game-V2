from turtle import Turtle

class Whiteline(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.01, stretch_len=1000)
        self.penup()
        self.goto(0, 260)