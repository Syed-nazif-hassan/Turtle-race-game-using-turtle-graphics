import turtle
from turtle import Turtle
from turtle import Screen
import random


screen = Screen()
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
goto_list = [-100, -70, -40, -10, 20, 50]
turtles = []
turtles_won = []
decider = 0
turtle_color = None
screen.setup(width=500, height=400)


try:
    turtle_color = screen.textinput(title="Make your guess", prompt="Which turtle will win the race? Enter a color: ").lower()
except AttributeError:
    pass


def race_decision(decide_r):
    if decide_r == 0:
        win_or_lose = "You lose!"
    else:
        win_or_lose = "You won!"
    if len(turtles_won) == 1:
        print(f"The {turtles_won[0]} turtle won the race. {win_or_lose}")
    elif len(turtles_won) == 2:
        print(f"The {turtles_won[0]} and {turtles_won[1]} turtle won the race. {win_or_lose}")
    else:
        all_colors_except_last_color = ", ".join(turtles_won[:len(turtles_won) - 1])
        last_color = turtles_won[len(turtles_won) - 1:]
        print(f"The {all_colors_except_last_color} and {last_color} turtle won the race. {win_or_lose}")


if turtle_color:
    try:
        if turtle_color in color_list:
            game_on = True
            for number in range(6):
                tim = Turtle(shape="turtle")
                tim.color(color_list[number])
                turtles.append(tim)
                tim.penup()
                tim.goto(-230, goto_list[number])
            while game_on:
                for t in turtles:
                    pace = random.randint(0, 10)
                    t.forward(pace)
                    if t.xcor() > 230:
                        game_on = False
                        winning_color = t.fillcolor()
                        turtles_won.append(winning_color)
            if turtle_color in turtles_won:
                decider = 1
                race_decision(decider)
            else:
                race_decision(decider)
            screen.exitonclick()
        else:
            print("Choose from these colors: (red, orange, yellow, green, blue, purple)")
            turtle.bye()
    except:
        pass
elif turtle_color == "" :
    print("Enter any of these colors: (red, orange, yellow, green, blue, purple)")
    turtle.bye()
else:
    turtle.bye()

