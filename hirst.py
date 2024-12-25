import turtle as t
import random
import colorgram

sammy = t.Turtle()

screen = t.Screen()
t.colormode(255)
sammy.shape("turtle")


colors = colorgram.extract("120123_r21786_g2048.jpg.webp", 7)


rgb_list = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_list.append((r,g,b))



new_list = [(238, 246, 243),(1, 13, 31), (52, 25, 17),(219, 127, 106),
            (0, 0, 0), (0, 0, 139), (139, 0, 0), (0, 100, 0), (128, 0, 128), (255, 140, 0),
            (64, 64, 64)]

sammy.speed("normal")
sammy.pensize(1)
sammy.penup()
sammy.setheading(245)
sammy.forward(300)
sammy.setheading(0)

for i in range(1, 100 + 1):
    sammy.dot(40, random.choice(new_list))
    sammy.forward(80)


    if i % 10 == 0:
        sammy.setheading(90)
        sammy.forward(80)
        sammy.setheading(180)
        sammy.forward(800)
        sammy.setheading(0)





screen.exitonclick()
