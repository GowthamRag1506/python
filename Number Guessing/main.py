import random

random_num = random.randint(1, 101)
print("Welcome to the number guessing game!!\nI'm thinking of a number between 1 and 100")
def game():
    level = input("Choose a difficulty 'easy' or 'hard' = ").lower()
    if level == "easy":
        print("you have 10 attempts to guess the number.\n")
        try:
            life = 10
            while life > 0:
                guess = int(input("Make a guess : "))
                if guess > random_num:
                    print("too high")
                    life -= 1
                    if life == 0:
                        print(f"GAME over , the number is {random_num}")
                elif guess < random_num:
                    print("Too low")
                    life -= 1
                    if life == 0:
                        print(f"GAME over , the number is {random_num}")
                elif guess == random_num:
                    print(f"You guessed it right!!, the number is {random_num}")
                    life = 0
        except:
            print("Invalid input")
            game()

    elif level == "hard":
        print("you have 5 attempts to guess the number.\n")
        try:
            life = 5
            while life > 0:
                guess = int(input("Make a guess : "))
                if guess > random_num:
                    print("too high")
                    life -= 1
                    if life == 0:
                        print(f"GAME over , the number is {random_num}")
                elif guess < random_num:
                    print("Too low")
                    life -= 1
                    if life == 0:
                        print(f"GAME over , the number is {random_num}")
                elif guess == random_num:
                    print(f"You guessed it right!!, the number is {random_num}")
                    life = 0
        except:
            print("Invalid input")
            game()


game()
