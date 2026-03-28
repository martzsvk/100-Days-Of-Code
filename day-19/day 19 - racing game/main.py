from turtle import Turtle,Screen
import random

colors = ["red", "orange", "gray", "green", "blue", "purple"]

x_position = - 225
y_position = - 175

all_turtles = []

is_race_on = False
# making more turtles
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.teleport(x_position, y_position + 50)
    y_position += 50
    new_turtle.penup()
    all_turtles.append(new_turtle)


# screen
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Make a bet", "Which turtle will win the race?(Ferrari, McLaren, Mercedes,"
"Sauber, Williams, Red Bull)")

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The {winning_color} turtle is a winner. ")
            else:
                print(f"You've lost. The {winning_color} turtle is a winner. ")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()