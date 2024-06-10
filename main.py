from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet!", prompt="Which Turtle will win the race? Pick a color: ")
colors = ["red", "orange", "yellow", "blue", "green", "purple"]
y_cor = [-100, -60, -20, 20, 60, 100]
all_turtles = []


for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_cor[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False

            win_color = turtle.pencolor()
            if win_color == user_bet:
                print(f"You've won! The {win_color} Turtle is the winner!")
            else:
                print(f"You've lost! The {win_color} Turtle is the winner!")

        rand_steps = random.randint(0, 10)
        turtle.forward(rand_steps)


screen.exitonclick()
