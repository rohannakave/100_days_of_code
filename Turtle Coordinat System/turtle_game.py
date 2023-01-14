from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
usr_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-75, -50, -25, 0, 25, 50]
all_turtle = []


for turtle_index in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

if usr_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == usr_bet:
                print(f"You win!!, {winning_color} turtle won the race.")
            else:
                print(f"You lost. {winning_color} turtle won the race.")
        rand_distance = randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()

