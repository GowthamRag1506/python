from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(0, -270)

    def go_up(self):
        self.forward(20)

    def go_down(self):
        self.back(20)

