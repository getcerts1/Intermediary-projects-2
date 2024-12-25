import turtle as t
import random


timmy = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors_list = []

def rgb_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    output = (r,g,b)
    return output

def color_list_gen(number_of_colors, lists):

    for i in range(number_of_colors + 1):
        random_color = (rgb_color())
        lists.append(random_color)

    for i, color in enumerate(lists):
        if lists.index(color) == 0:
            continue
        print(f"{i}:{color}")


color_list_gen(20, colors_list)

directions = [0, 90,180,270]
timmy.pensize(20)
timmy.speed("fastest")

for i in range(100):
    timmy.pencolor(random.choice(colors_list))
    timmy.setheading(random.choice(directions))
    timmy.forward(40)


screen.exitonclick()