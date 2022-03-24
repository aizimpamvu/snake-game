from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake Game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
# Creating our snake

segments = []
for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)

game_is_on=True
while game_is_on:
    for segment in segments:
        segment.forward(20)
screen.exitonclick()
