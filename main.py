from turtle import Turtle, Screen
import random

s = Screen()
is_race_on = False
s.setup(width=400, height= 500)
my_son = s.textinput(title="My son bet", prompt= "Which color is the winner")
myself = s.textinput(title="My bet", prompt="Which color is the winner")

colors = ["blue", "indigo", "red", "orange", "green", "black"]
total_turtle = []
x_pos = [-125,-75,-25,25,75,125 ]

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.setheading(270)
    new_turtle.speed("fastest")
    new_turtle.penup()
    new_turtle.goto(x=x_pos[turtle_index], y=230)
    total_turtle.append(new_turtle)

if my_son and myself:
    is_race_on = True

while is_race_on:
    for turtle in total_turtle:
        if turtle.ycor() < -230:
            is_race_on = False

            if not turtle.pencolor() == myself and not turtle.pencolor() == my_son:
                print(f"You both have lost. The {turtle.pencolor()} was the winner")
            elif my_son == turtle.pencolor():
                print(f"My son's won. The {my_son} is the winner")
            else:
                print(f"I've won. The {myself} is the winner")


        pace = random.randint(0,10)
        turtle.forward(pace)




s.exitonclick()