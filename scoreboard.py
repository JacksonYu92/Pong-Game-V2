from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 22, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0,300)
        self.write("Welcome to Jackson's Pong Game", align=ALIGNMENT, font=("Courier", 30, "normal"))
        self.goto(-250, 225)
        self.write(f"Left hand\n    {self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(250, 225)
        self.write(f"Right hand\n     {self.r_score}", align=ALIGNMENT, font=FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()