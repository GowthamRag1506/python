from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.snake()

    def add_segments(self, pos):
        tur = Turtle(shape="square")
        tur.color('white')
        tur.penup()
        self.segments.append(tur)
        tur.goto(pos)

    def snake(self):
        for pos in POSITION:
            self.add_segments(pos)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for index in range((len(self.segments)) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)
        self.segments[0].forward(20)

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
