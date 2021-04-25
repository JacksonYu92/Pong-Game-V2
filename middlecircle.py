from turtle import Turtle


class Middlecircle(Turtle):
    def __init__(self):
        super().__init__()
        self.white()
        self.black()

    def white(self):
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=8, stretch_len=8)
        self.penup()

    def black(self):
        self.shape("circle")
        self.color("black")
        self.shapesize(stretch_wid=7, stretch_len=7)
        self.penup()
