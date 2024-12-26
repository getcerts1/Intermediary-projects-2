import turtle as t

cursor = t.Turtle()
screen = t.Screen()
t.listen()


pen_size = screen.numinput("Pen Size", "Enter a value (1-10):", minval=1, maxval=10)
if pen_size is None:  # Handle 'Cancel' button or no input
    pen_size = 1
cursor.pensize(int(pen_size))


def move_right():
    cursor.setheading(0)
    cursor.forward(40)
    cursor.pensize(pen_size)


def move_left():
    cursor.setheading(180)
    cursor.forward(40)
    cursor.pensize(pen_size)

def move_up():
    cursor.setheading(90)
    cursor.forward(40)
    cursor.pensize(pen_size)

def move_down():
    cursor.setheading(270)
    cursor.forward(40)
    cursor.pensize(pen_size)

def clear_screen():
    cursor.reset()

def pen_up():
    cursor.penup()

screen.listen()
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(move_up, "w")
screen.onkey(move_down, "s")
screen.onkey(clear_screen, "c")
screen.onkey(pen_up, "Up")


screen.exitonclick()