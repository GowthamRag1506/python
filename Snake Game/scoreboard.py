from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.write(f"Score : {self.score}",align='center',font=('Arial',20,'normal'))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}",align='center',font=('Arial',20,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game over\nYour Score :{self.score} ',align='center',font=('Arial',20,'normal'))
