from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500,height=500)
clr = ['red','green','yellow','purple','blue','orange']
tur = ['t1','t2','t3','t4','t5','t6']
x = -230
y = -70
for i in range(len(tur)):
    tur[i] = Turtle(shape='turtle')
    tur[i].color(clr[i])

for j in tur:
    j.penup()
    j.setpos(x,y)
    y += 40
guess = screen.textinput("Guess who will win",'Enter turtle color:')


def start_race():
    continue_game = True
    while continue_game:
        for k in tur:
            if k.xcor() > 230:
                winner = k
                if guess == winner.pencolor():
                    print(f"guess : {guess}\nwinner: {winner.pencolor()}\nYou guessed it right!!!")
                else:
                    print(f"guess : {guess}\nwinner is {winner.pencolor()}\nYou guessed it Wrong!!!")
                continue_game = False
                break
            num = random.randint(0,20)
            k.forward(num)


screen.listen()
screen.onkey(key='space', fun=start_race)
screen.exitonclick()
