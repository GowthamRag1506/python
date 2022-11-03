from turtle import Turtle,Screen
from paddle import Paddle,Ball,Scoreboard
import time

screen = Screen()
ball = Ball()
speed = .1
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle(270,0)
l_paddle = Paddle(-270,0)
l_score = Scoreboard(-50,270)
r_score = Scoreboard(50,270)
screen.tracer(1)
play = True
screen.listen()
screen.onkeypress(l_paddle.go_up,'w')
screen.onkeypress(l_paddle.go_down,'s')
screen.onkeypress(r_paddle.go_up,'Up')
screen.onkeypress(r_paddle.go_down,'Down')
while play:
    game_on = True
    screen.tracer(1)
    while game_on:
        time.sleep(speed)
        ball.move()
        #BALL COLLIDES WITH TOP WALL
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        # ball collides with paddle
        if (ball.distance(l_paddle) < 50 and ball.xcor() < -250) or (ball.distance(r_paddle) < 50 and ball.xcor() > 250):
            ball.bounce_x()
            if speed >= 0.01:
                speed -= .01
        # ball collides with wall, update score
        if ball.xcor() < -270:
            r_score.score += 1
            r_score.update()
            screen.tracer(0)
            ball.goto(0,0)
            ball.a *= -1
            game_on = False
            if l_score.score >= 20:
                play = False

        if ball.xcor() > 270:
            l_score.score += 1
            l_score.update()
            screen.tracer(0)
            ball.goto(0,0)
            ball.a *= -1
            game_on = False
            if l_score.score >= 20:
                play = False

screen.exitonclick()
