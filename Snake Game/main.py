from turtle import Screen
from turtle import Turtle
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)
my_snake = Snake()
screen.listen()
screen.onkey(my_snake.right,'Right')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
game_on = True
while game_on:
    screen.update()
    time.sleep(0.10)
    my_snake.move()

screen.exitonclick()