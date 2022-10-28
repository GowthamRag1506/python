#rock paper scissors
import random
a = int(input("What do you choose? 0 for Rock , 1 for  paper, 2 for scissors :"))
options = ["rock", "paper", "scissor"]
c = options[a]
print(f"Your choice is : {c}")
computer = random.choice(options)
print(f"Computer choice is : {computer}")
if c == "rock" and computer == "scissor":
    print("You WON!!!!")
elif c == "paper" and computer == "rock":
    print("You WON!!!!")
elif c == "scissor" and computer == "paper":
    print("You WON!!!!")
else:
    print("YOU LOOSE")
