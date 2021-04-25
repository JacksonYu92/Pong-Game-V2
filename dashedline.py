from turtle import Turtle


class Dashedline(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=26, stretch_len=0.01)
        self.penup()
        self.goto(0, -35)


