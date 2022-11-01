from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
my_snake = Snake()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)
screen.listen()
screen.onkey(my_snake.right, 'Right')
screen.onkey(my_snake.left, 'Left')
screen.onkey(my_snake.up, 'Up')
screen.onkey(my_snake.down, 'Down')
game_on = True
food = Food()
score = Score()
while game_on:
    screen.update()
    time.sleep(0.10)
    my_snake.move()
    if my_snake.segments[0].distance(food) < 15:
        food.refresh()
        my_snake.extend()
        score.update_score()
    if my_snake.segments[0].xcor() > 280 or my_snake.segments[0].ycor() > 280 or my_snake.segments[0].xcor() < -280 or \
            my_snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()
    for seg in my_snake.segments:
        if seg == my_snake.segments[0]:
            pass
        elif my_snake.segments[0].distance(seg) < 10:
            game_on = False
            score.game_over()
screen.exitonclick()
