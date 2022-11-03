from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_wid=3,stretch_len=.50)
        self.penup()
        self.goto(x,y)

    def go_up(self):
        if self.ycor() < 260:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def go_down(self):
        if self.ycor() > -260:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)


class Scoreboard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.penup()
        self.goto(x,y)
        self.write(f'{self.score}',align="center",font=('Arial',20,""))

    def update(self):
        self.clear()
        self.write(f'{self.score}',align="center",font=('Arial',20,""))



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('circle')
        self.penup()
        self.turtlesize(stretch_wid=1,stretch_len=1)
        self.a = 10
        self.b = 10

    def move(self):
        x = self.xcor() + self.a
        y = self.ycor() + self.b
        self.goto(x,y)

    def bounce_y(self):
        self.b = self.b * -1

    def bounce_x(self):
        self.a = self.a * -1



