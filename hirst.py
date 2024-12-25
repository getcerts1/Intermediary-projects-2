import turtle as t
import random
import colorgram
from randomwalk import colors_list, color_list_gen

sammy = t.Turtle()

screen = t.Screen()
t.colormode(255)
sammy.shape("turtle")


colors = colorgram.extract("120123_r21786_g2048.jpg.webp", 7)
print(colors)

rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r,g,b))


print(rgb_list)
new_list = [(238, 246, 243),(1, 13, 31), (52, 25, 17),(219, 127, 106),
            (0, 0, 0), (0, 0, 139), (139, 0, 0), (0, 100, 0), (128, 0, 128), (255, 140, 0),
            (64, 64, 64)]


sammy.pensize(1)
sammy.penup()
sammy.backward(200)
sammy.right(90)
sammy.forward(200)
sammy.setheading(0)
for i in range(100):
    if 100 % i == 0:
        sammy.left(20)
        sammy.left(150)
        sammy.setheading(0)
    sammy.dot(20, random.choice(new_list))
    sammy.forward(20)



screen.exitonclick()
