import turtle
import turtle as t
import random


timmy = t.Turtle()
#screen = t.Screen()

static_colors = [
    "black", "red", "blue", "green", "purple",
    "orange", "dark cyan", "magenta", "brown",
    "dark slate gray", "cyan", "yellow", "gold"
]
dynamic_colors = [

]


def rgb_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    output = f'({r},{g},{b})'
    return output

def color_list_gen(number_of_colors):
    for i in range(number_of_colors):
        random_color = (rgb_color())
        colors.append(random_color)

    for i, color in enumerate(colors):
        if colors.index(color) == 0:
            continue
        print(f'color {i}: {color}')