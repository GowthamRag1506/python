from turtle import Turtle
import random
COLORS = ['red','yellow','orange','blue','green','purple']


class Cars():
    def __init__(self):
        self.cars = []

    def create_car(self):
        x = random.randint(1,6)
        if x == 3:
            new_car = Turtle('square')
            new_car.turtlesize(stretch_wid=1,stretch_len=3)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(450,random.randint(-150,150))
            self.cars.append(new_car)
