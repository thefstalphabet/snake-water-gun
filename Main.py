# here we import random inbuld module
import random

#Game heading
print("*** WELCOME TO THE -SNAKE,WATER,GUN- GAME ***")
print("You have 10 chance to win this game")

# humna and computer points
your_point = 0
computer_point = 0

# starting of while loop
chance = 1
while (chance<11):
    print("This is atempt number ->",chance)
    chance = chance + 1

    # this is random word choice list and module function
    lst = ["s", "w", "g"]
    choice = random.choice(lst)

    # input for what user take s,w,g
    snake = "s"
    water = "w"
    gun = "g"
    first_input = input(f"Press {snake} for snake, Press {water} for water, Press {gun} for gun\n")


    # conditions
    if first_input==choice:
        print("computer select", choice)
        print("Game is tie 0 points to each\n")

    elif first_input is snake and choice is water:
        print("computer select", choice)
        print("You win +1 point to you\n")
        your_point = your_point + 1


    elif first_input is snake and choice is gun:
        print("computer select", choice)
        print("You lose +1 point to computer\n")
        computer_point = computer_point + 1


    elif first_input is water and choice is snake:
        print("computer select", choice)
        print("You lose +1 point to computer\n")
        computer_point = computer_point + 1


    elif first_input is water and choice is gun:
        print("computer select", choice)
        print("You lose +1 point to computer\n")
        computer_point = computer_point + 1


    elif first_input is gun and choice is snake:
        print("computer select", choice)
        print("You win +1 point to you\n")
        your_point = your_point + 1

    elif first_input is gun and choice is water:
        print("computer select", choice)
        print("You win +1 point to you\n")
        your_point = your_point + 1


# result statments
print("*** RESULTS ***\n")
print("Total human point is ", your_point)
print("Total computer point is ", computer_point)

# result conditons
if your_point>computer_point:
    print("You win the game")
elif computer_point>your_point:
    print("Computer is win the game ")
