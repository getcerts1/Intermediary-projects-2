import turtle as t

cursor = t.Turtle()
screen = t.Screen()
t.listen()
screen.listen()


def move_right():
    cursor.setheading(0)
    cursor.forward(40)

def move_left():
    cursor.setheading(180)
    cursor.forward(40)

def move_up():
    cursor.setheading(90)
    cursor.forward(40)

def move_down():
    cursor.setheading(270)
    cursor.forward(40)

def clear_screen():
    cursor.reset()

def pen_up():
    cursor.penup()

def set_pen_size():


screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(clear_screen, "c")




screen.exitonclick()