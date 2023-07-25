from turtle import Turtle as t
from turtle import Screen as s
import random

screen = s()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
goto_list = [-100, -70, -40, -10, 20, 50]
turtles = []
screen.setup(width=500, height=400)
screen.screensize(canvwidth=500, canvheight=400)
turtle_color = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Enter a color: ")
for number in range(6):
    tim = t(shape="turtle")
    tim.color(color_list[number])
    turtles.append(tim)
    tim.penup()
    tim.goto(-230, goto_list[number])

if turtle_color:
    if turtle_color in color_list:
        game_on = True

while game_on:

    for t in turtles:
        pace = random.randint(0, 10)
        t.forward(pace)
        if t.xcor() > 230:
            game_on = False
            winning_color = t.fillcolor()
            if turtle_color == winning_color:
                print(f"The {winning_color} turtle won the race. You won!")
            else:
                print(f"The {winning_color} turtle won the race. You lose!")

screen.exitonclick()
