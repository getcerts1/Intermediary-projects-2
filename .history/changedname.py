from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()

timmy.speed("fast")
colors = ["red", "green", "blue", "cyan", "violet", "indigo", "black"]

def change_color():
    random_color = random.choice(colors)
    timmy.color(random_color)
    colors.remove(random_color)

change_color()
for i in range(3):
    timmy.forward(100)
    timmy.right(120)

change_color()
for i in range(4):
    timmy.forward(100)
    timmy.right(90)

change_color()
for i in range(5):
    timmy.forward(100)
    timmy.right(72)

change_color()
for i in range(6):
    timmy.forward(100)
    timmy.right(60)

change_color()
for i in range(7):
    timmy.forward(100)
    timmy.right(51.42)

change_color()
for i in range(8):
    timmy.forward(100)
    timmy.right(45)

change_color()
for i in range(9):
    timmy.forward(100)
    timmy.right(40)


screen.exitonclick()