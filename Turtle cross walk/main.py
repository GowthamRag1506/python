from turtle import Screen
from player import Player
from cars import Cars
import time


screen = Screen()
car = Cars()
game_over = Screen()

screen.tracer(0)
player = Player()
screen.setup(width=900,height=600)

screen.listen()
screen.onkeypress(player.go_up,'Up')
screen.onkeypress(player.go_down,'Down')
game_on = True
x = 10
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    for each in car.cars:
        each.back(x)
    for each in car.cars:
        if player.distance(each) < 30:
            game_on = False

screen.exitonclick()
