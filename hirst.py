import turtle as t
import random
import colorgram

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

sammy.speed("fastest")
sammy.pensize(1)
sammy.penup()
sammy.backward(150)
sammy.right(90)
sammy.forward(150)
sammy.setheading(0)

for i in range(100):
    try:
        if i % 10 == 0:
            sammy.left(90)
            sammy.forward(40)
            sammy.left(90)
            sammy.forward(400)
            sammy.setheading(0)
    except ZeroDivisionError:
        continue
    sammy.forward(40)
    sammy.dot(20, random.choice(new_list))




screen.exitonclick()
